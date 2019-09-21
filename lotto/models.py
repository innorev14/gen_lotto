from django.db import models

# Create your models here.
class MyLotto(models.Model):
    username = models.CharField(max_length=20)
    round = models.PositiveIntegerField()
    gamemethod = models.IntegerField()
    gameamout = models.PositiveIntegerField()
    gamemoney = models.PositiveIntegerField()

class GenLotto(models.Model):
    user = models.ForeignKey(MyLotto, on_delete=models.CASCADE)
    num1 = models.PositiveIntegerField()
    num2 = models.PositiveIntegerField()
    num3 = models.PositiveIntegerField()
    num4 = models.PositiveIntegerField()
    num5 = models.PositiveIntegerField()
    num6 = models.PositiveIntegerField()

class Winnum(models.Model):
    round = models.PositiveIntegerField()
    num1 = models.PositiveIntegerField()
    num2 = models.PositiveIntegerField()
    num3 = models.PositiveIntegerField()
    num4 = models.PositiveIntegerField()
    num5 = models.PositiveIntegerField()
    num6 = models.PositiveIntegerField()
    bounusnum = models.PositiveIntegerField()
    winneramount = models.CharField(max_length=10)
    perprize = models.CharField(max_length=20)
    winmethod = models.CharField(max_length=30)
