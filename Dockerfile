FROM python:3.7-slim AS geocode

COPY . /compose

WORKDIR /compose

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "/compose:/compose/geocode:/compose/geocode/app:/compose/geocode/core:/compose/geocode/scripts:/compose/geocode/static:${PYTHONPATH}"
ENV PATH "${PATH}:${PYTHONPATH}"

RUN pip3 install --upgrade pip
RUN apt update
RUN apt install build-essential -y
RUN pip3 install pipenv --upgrade 
RUN set -ex && pipenv install -r /compose/geocode/requirements.txt --python 3.7 --ignore-pipfile --skip-lock

CMD [\
    "pipenv",\
    "run",\
    "gunicorn",\
    "geocode.app.wsgi:application",\
    "-w", "2",\
    "--threads", "2",\
    "--access-logfile=-",\
    "-b", "0.0.0.0:8000"\
    ]