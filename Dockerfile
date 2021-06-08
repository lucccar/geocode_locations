FROM python:3.7-slim

COPY . /geocode
WORKDIR /geocode

ENV PYTHONUNBUFFERED 1

RUN "python manage.py bootdata"

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]