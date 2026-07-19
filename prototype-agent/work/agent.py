import os       # Работа с переменными окружения и путями
import uuid     # Генерация уникальных идентификаторов thread_id
import json     # Чтение JSON-конфига MCP
import time     # Замеры времени работы агента и tool-call'ов
import asyncio  # Запуск и управление асинхронным кодом

from contextlib import AsyncExitStack
from dotenv import load_dotenv

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools

from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver

from langchain_core.tools import StructuredTool
from langchain_gigachat.chat_models import GigaChat


load_dotenv()


def make_llm():
    """
    Создание LLM.
    Оставляем GigaChat, как в исходном коде.
    """
    return GigaChat(
        credentials=os.getenv("CREDENTIALS_M2"),
        scope=os.getenv("SCOPE_M2"),
        model=os.getenv("MODEL_M2"),
        verify_ssl_certs=os.getenv("VERIFY_SSL_CERTS_M2"),
        temperature=float(os.getenv("TEMPERATURE", "0.2")),
    )


def load_mcp_config() -> dict:
    config_path = os.path.join(
        os.path.dirname(__file__),
        "config.json"
    )

    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


def instrument_tools(tools, run_stats: dict):
    """
    Оборачивает MCP-инструменты в логирующую оболочку.

    Что логируется:
    - номер tool-call'а;
    - время до первого tool-call'а;
    - начало и конец каждого вызова инструмента;
    - длительность выполнения каждого инструмента.
    """
    wrapped_tools = []

    for tool in tools:
        tool_name = getattr(tool, "name", "unknown_tool")
        tool_description = getattr(tool, "description", "")
        tool_args_schema = getattr(tool, "args_schema", None)

        async def timed_func(*args, _tool=tool, _tool_name=tool_name, **kwargs):
            now = time.perf_counter()

            run_stats["tool_calls"] += 1
            tool_index = run_stats["tool_calls"]

            if (
                run_stats["started_at"] is not None
                and run_stats["first_tool_delay"] is None
            ):
                run_stats["first_tool_delay"] = now - run_stats["started_at"]
                print(
                    f"⏱ До первого tool-call: "
                    f"{run_stats['first_tool_delay']:.3f} сек"
                )

            print(f"➡️ START tool #{tool_index}: {_tool_name}")
            t0 = time.perf_counter()

            try:
                # LangChain может передать либо один dict-параметр,
                # либо именованные параметры. Обрабатываем оба варианта.
                if args and not kwargs:
                    tool_input = args[0]
                else:
                    tool_input = kwargs

                try:
                    print(
                        "🧾 Tool input:",
                        json.dumps(tool_input, ensure_ascii=False, indent=2)
                    )
                except Exception:
                    print("🧾 Tool input:", tool_input)

                result = await _tool.ainvoke(tool_input)
                return result

            except Exception as e:
                print(f"❌ ERROR tool #{tool_index}: {_tool_name}: {e}")
                raise

            finally:
                dt = time.perf_counter() - t0
                print(f"⬅️ END   tool #{tool_index}: {_tool_name} ({dt:.3f} сек)")

        wrapped_tool = StructuredTool.from_function(
            coroutine=timed_func,
            name=tool_name,
            description=tool_description,
            args_schema=tool_args_schema,
        )

        wrapped_tools.append(wrapped_tool)

    return wrapped_tools


async def load_tools_from_persistent_sessions(
    mcp_client: MultiServerMCPClient,
    mcp_servers: dict,
    stack: AsyncExitStack,
):
    """
    Открывает постоянные MCP-сессии один раз
    и загружает инструменты из этих сессий.

    Это главное отличие от простого await mcp_client.get_tools().
    Теперь серверы не пересоздаются на каждый отдельный вызов tools.
    """
    all_tools = []

    print("=== MCP сервера из конфига ===")

    for server_name, cfg in mcp_servers.items():
        print(
            f"- {server_name} "
            f"(transport={cfg.get('transport')}, "
            f"command={cfg.get('command')}, "
            f"url={cfg.get('url')})"
        )

    print("\n=== Инструменты по каждому серверу ===")

    for server_name in mcp_servers.keys():
        try:
            session = await stack.enter_async_context(
                mcp_client.session(server_name)
            )

            server_tools = await load_mcp_tools(
                session,
                server_name=server_name,
            )

            print(f"\nСервер: {server_name}")

            if not server_tools:
                print("  (нет инструментов или сервер не ответил)")
                continue

            for tool in server_tools:
                print(f" • {tool.name} — {getattr(tool, 'description', '')}")

                args_schema = getattr(tool, "args_schema", None)

                if args_schema is None:
                    print("   args_schema: отсутствует")
                else:
                    try:
                        if isinstance(args_schema, dict):
                            print(
                                json.dumps(
                                    args_schema,
                                    ensure_ascii=False,
                                    indent=2
                                )
                            )
                        elif hasattr(args_schema, "model_json_schema"):
                            print(
                                json.dumps(
                                    args_schema.model_json_schema(),
                                    ensure_ascii=False,
                                    indent=2
                                )
                            )
                        elif hasattr(args_schema, "schema"):
                            print(
                                json.dumps(
                                    args_schema.schema(),
                                    ensure_ascii=False,
                                    indent=2
                                )
                            )
                        else:
                            print(f"   args_schema type: {type(args_schema)}")
                            print(args_schema)
                    except Exception as e:
                        print(f"   Не удалось вывести args_schema: {e}")

            all_tools.extend(server_tools)

        except Exception as e:
            print(f"\nСервер: {server_name}")
            print(f"  Ошибка при подключении или загрузке инструментов: {e}")

    print("\n------------------------------")

    return all_tools


async def main():
    config_data = load_mcp_config()

    mcp_servers = config_data.get("mcpServers", {})
    if not mcp_servers:
        raise RuntimeError("В MCP-конфиге не найден ключ 'mcpServers' или он пустой.")

    mcp_client = MultiServerMCPClient(mcp_servers)

    run_stats = {
        "started_at": None,
        "first_tool_delay": None,
        "tool_calls": 0,
    }

    async with AsyncExitStack() as stack:
        # 1. Открываем persistent MCP-сессии и загружаем инструменты
        tools = await load_tools_from_persistent_sessions(
            mcp_client=mcp_client,
            mcp_servers=mcp_servers,
            stack=stack,
        )

        # 2. Оборачиваем инструменты логированием
        tools = instrument_tools(tools, run_stats)

        # 3. Создаём агента
        agent = create_react_agent(
            model=make_llm(),
            tools=tools,
            checkpointer=InMemorySaver(),
        )

        # Один thread_id на всю интерактивную сессию,
        # чтобы checkpointer сохранял контекст диалога.
        thread_id = uuid.uuid4().hex

        while True:
            user_input = input("пользователь: ").strip()

            if not user_input:
                continue

            if user_input.lower() in {"exit", "quit", "выход"}:
                print("Завершение работы.")
                break

            task = f"""
Ты интеллектуальный помощник. Действуй в соответствии с задачами,
выдаваемыми пользователем.

Если выполнение задачи требует действий, которые можно выполнить через инструменты,
предоставленные через Model Context Protocol (MCP), используй эти инструменты.

Если tool вернул ошибку — не выдумывай результат, а объясни проблему
или попробуй исправить причину, если это возможно.
Не подменяй выход tool своими измышлениями, например если ответ tool это not found,
то говори что tool вернул not found, а не придумывай ответ на вопрос пользователя.

Текущая задача от пользователя: {user_input}
"""

            base_config = {
                "configurable": {"thread_id": thread_id},
                "recursion_limit": 20,
            }

            # Сброс статистики перед каждым пользовательским запросом
            run_stats["started_at"] = time.perf_counter()
            run_stats["first_tool_delay"] = None
            run_stats["tool_calls"] = 0

            result = await agent.ainvoke(
                {"messages": [{"role": "user", "content": task}]},
                config=base_config,
            )

            total_time = time.perf_counter() - run_stats["started_at"]

            print(f"\n⏱ Общее время запроса: {total_time:.3f} сек")
            print(f"🔢 Всего tool-вызовов: {run_stats['tool_calls']}")

            if run_stats["first_tool_delay"] is None:
                print("🤖 Tool-вызовов не было")
            else:
                tail_time = total_time - run_stats["first_tool_delay"]
                print(
                    f"⏱ Время после первого tool-call до конца: "
                    f"{tail_time:.3f} сек"
                )

            # Дополнительный вывод ответов инструментов из истории сообщений
            for msg in result["messages"]:
                if getattr(msg, "type", "") == "tool":
                    tool_name = getattr(msg, "name", "")
                    tool_content = str(getattr(msg, "content", ""))

                    print(
                        f"🔧 Tool response ({tool_name}): "
                        f"{tool_content[:800]}"
                    )

            print("\nРезультат:", result["messages"][-1].content)
            print()


if __name__ == "__main__":
    asyncio.run(main())

    #     "filesystem": {
    #   "command": "npx.cmd",
    #   "args": [
    #     "-y",
    #     "@modelcontextprotocol/server-filesystem",
    #     "D:/Works/учёба/ВКР/code/agent",
    #     "D:/Works/учёба/ВКР/GpDelphiUnits_mini/src"
    #   ],
    #   "transport": "stdio"
    # }