from django.shortcuts import render
from django.http import HttpResponse
from django.db import models

# Create your views here.

def index(request):
    return HttpResponse('This is Homepage')

def detail(request,userid):
    return HttpResponse('The userid is %s'%userid)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
