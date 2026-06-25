import streamlit as st
from langchain.llms import OpenAI
#id 006
# from langchain_community.chat_models.gigachat import GigaChat
# from langchain.schema import HumanMessage
st.set_page_config(page_title="🦜🔗 Quickstart App")
st.title('🦜🔗 Quickstart App')

openai_api_key = st.sidebar.text_input('OpenAI API Key')
#id 007
# gigaChatKey = st.sidebar.text_input('GigaChat: API Key')

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))
  #id 003
  # llm1 = GigaChat(credentials=gigaChatKey, scope="GIGACHAT_API_PERS", model="GigaChat", verify_ssl_certs=False, streaming=False)
  # user_input = f"User: {$INPUT}"
  # message = [HumanMessage(content=user_input)]
  # st.info(f"GigaChat: {(llm1(message)).content}")

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
  #id 008
  # gigaChatKey
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
  #id 008
  # gigaChatKey
    generate_response(text)