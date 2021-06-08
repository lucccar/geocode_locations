FROM python:slim




RUN "python manage.py bootdata"

CMD ["python", "manage.py", "runserver"]