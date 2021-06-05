from django.core.management.base import BaseCommand
from subprocess import Popen
from sys import stdout, stdin, stderr
import time
import csv
from core.models import Customer


class Command(BaseCommand):
    help = 'Bootstrap command to populate the datebase'
    commands = [
        "python manage.py migrate",
        "python manage.py makemigrations",
        "python manage.py migrate --run-syncdb"
        ]

    def handle(self, *args, **kwargs):
        # Perform migrations of the database models and dbfile
        for command in self.commands:
            self.stdout.write(self.style.SUCCESS('$ ' + command))
            Popen(command, shell=True, stdin=stdin, stdout=stdout, stderr=stderr)
            time.sleep(1)

        # Perform the database population
        file_path = 'customers.csv'
        with open(file_path, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                id,first_name,last_name,email,gender,company,city,title = row
                customer = Customer(id,first_name,last_name,email,gender,company,city,title, None, None)
                customer.save()

            self.stdout.write(self.style.SUCCESS('Database populated'))
            