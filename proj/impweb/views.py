from django.shortcuts import render

from django.db import models
# Create your views here.
class Test(models.Model):
    name = models.CharField(max_length=20)
