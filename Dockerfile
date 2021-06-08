FROM python:3.7-slim

COPY . /geocode
WORKDIR /geocode

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# RUN python manage.py bootdata


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]