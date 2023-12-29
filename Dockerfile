FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip setuptools wheel

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/dev_requirements.txt

ENV PYTHONUNBUFFERED=1