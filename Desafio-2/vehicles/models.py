from django.utils import timezone
import datetime
from django.db import models

# TODO: alguns campos devem ser notnull

# Create your models here.

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     def __str__(self):
#       return self.question_text

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#         return self.choice_text


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
