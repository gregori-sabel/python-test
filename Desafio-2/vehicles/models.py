from django.utils import timezone
import datetime
from django.db import models

# TODO: alguns campos devem ser notnull


class User(models.Model):
    name = models.CharField(max_length=50)
    card = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Vehicle(models.Model):
    plate = models.CharField(max_length=10)
    model = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.plate
