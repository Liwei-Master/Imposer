# modify the model----1. modify 2. python manage.py makemigrations ( record this modification)
# 3. python manage.py migrate (update into database)

# shell operation(API): 1. python manage.py shell 2. from poll.models import Question, Choice 3. Question.objects.all()

from django.db import models

import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('data published')
    topic = models.CharField(max_length=20, default="other")
    limit_of_voters = models.IntegerField(default=0)
    launcher = models.CharField(max_length=20, default="Liwei")

    def __str__(self):
        return self.question_text

    def number_of_votes(self):
        amount = len(self.reason_set.all())
        return amount

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    # modify the filed name of this attribute
    was_published_recently.short_description = 'Published recently?'



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Reason(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    reason_text = models.CharField(max_length=400, default="None")
    choice = models.CharField(max_length=100)


