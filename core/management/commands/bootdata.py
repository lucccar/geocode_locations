from django.core.management.base import BaseCommand
from subprocess import Popen
from sys import stdout, stdin, stderr
import time
import csv
from core.models import Customer


class Command(BaseCommand):
    help = 'Bootstrap command to populate the datebase'
    commands = ["python manage.py migrate"]

    def handle(self, *args, **kwargs):

        for command in self.commands:
            print("$ " + command)
            proc = Popen(command, shell=True, stdin=stdin, stdout=stdout, stderr=stderr)
            # proc_list.append(proc)

        time.sleep(1)

        file_path = 'customers.csv'
        with open(file_path, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                id,first_name,last_name,email,gender,company,city,title = row
                customer = Customer(id,first_name,last_name,email,gender,company,city,title)
                customer.save()
            self.stdout.write("Database populated")
            