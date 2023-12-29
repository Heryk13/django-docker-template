FROM ubuntu

RUN mkdir /app

RUN apt-get update && apt-get install -y python3 python3-pip

COPY . /app

RUN pip3 install pipenv

RUN pip3 install pyxel

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["python3", "/app/src/core/manage.py", "runserver", "0.0.0.0:8000"]