from django.db import models


class Customer(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.CharField(max_length=35)
    gender = models.CharField(max_length=6)
    company = models.CharField(max_length=15)
    city = models.CharField(max_length=25)
    title = models.CharField(max_length=30)
    latitude = models.FloatField(max_length=11, null=True, blank=True)
    longitude = models.FloatField(max_length=11, null=True, blank=True)
