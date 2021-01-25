FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY /preprocessing /preprocessing
COPY ./app /app

WORKDIR /app
RUN pip3 install -e ../preprocessing

