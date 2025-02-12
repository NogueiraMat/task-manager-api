FROM python:3.10

WORKDIR /app

COPY ./app /app/

COPY ./requirements.txt requirements.txt

RUN apt-get update -y && apt-get upgrade -y

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]