from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)



# class User(models.Model):
#     name = models.CharField(max_length=50)
#     card = models.CharField(max_length=10)


# class Vehicle(models.Model):
#     plate = models.CharField(max_length=10)
#     model = models.CharField(max_length=30)
#     description = models.CharField(max_length=50)
#     customer = models.ForeignKey(User, on_delete=models.CASCADE)
