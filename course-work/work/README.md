для запуска преобразователя
docker build -t {project-updater} .
docker run --rm -v "${PWD}:/data" -w /data {project-updater} {rules}.json {ProgramForConversion}.py {output}.py

для запуска проекта
docker build -t {my-streamlit} .
docker run --rm -p 8501:8501 -v "${PWD}:/app" {my-streamlit} {output}.py