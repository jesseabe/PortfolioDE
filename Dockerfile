FROM python:3.12
COPY . /src
WORKDIR /src
EXPOSE 8501
ENTRYPOINT ["poetry","run", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
# ENTRYPOINT ["poetry","run", "python", "main.py"]