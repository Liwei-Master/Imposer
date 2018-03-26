from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db import models
from .models import Choice, Question, Reason
from login.models import User
from django.urls import reverse # in case users resend the form
import datetime
import time
from django.utils.timezone import utc
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# test: python manage.py runserver 127.0.0.1:8000



from django.template import loader

# Create your views here.

def index(request):
    # question_list = Question.objects.order_by('-pub_date')[:5]
    question_list = Question.objects.order_by('-pub_date')
    question_pages = Paginator(question_list, 7)
    page = request.GET.get('page', '1')
    polls = question_pages.page(page)

    next_page = 1
    previous_page = 1
    if polls.has_next():
        next_page = polls.next_page_number()
    if polls.has_previous():
        previous_page = polls.previous_page_number()

    poll_number = len(Question.objects.all())
    user_number = len(User.objects.all())

    context = {
        'poll_number'  : poll_number,
        'user_number': user_number,
        'previous_page'    : previous_page,
        'next_page'    : next_page,
        'first_page'    : 1,
        'last_page'    : question_pages.num_pages,
        'polls'        : polls,

    }
    return render(request, 'poll/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    arguments = question.reason_set.all().order_by('reason_text')
    # Show 3 contacts per page
    pages = Paginator(arguments, 3)
    # GET method
    page = request.GET.get('page', '1')
    argument = pages.page(page)

    return render(request, 'poll/detail.html', {'question': question, 'arguments':argument})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    arguments = question.reason_set.all()
    # Show 3 contacts per page
    pages = Paginator(arguments, 3)
    # GET method
    page = request.GET.get('page', '1')
    argument = pages.page(page)
    return render(request, 'poll/results.html', {'question': question, 'arguments':argument})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if not request.session.get('is_login', None):
        arguments = question.reason_set.all()
        # Show 3 contacts per page
        pages = Paginator(arguments, 3)
        # GET method
        page = request.GET.get('page', '1')
        argument = pages.page(page)

        return render(request, 'poll/detail.html', {
            'question': question,
            'error_message': "Please login first",
            'arguments': argument,
        })
    if request.POST:
        reason = request.POST['reason']
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 发生choice未找到异常时，重新返回表单页面，并给出提示信息
        return render(request, 'poll/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:

        reason_db = Reason(question=question, reason_text=reason, choice= selected_choice.choice_text)
        reason_db.save()
        selected_choice.votes += 1
        selected_choice.save()
        # 成功处理数据后，自动跳转到结果页面，防止用户连续多次提交。
        return HttpResponseRedirect(reverse('poll:results', args=(question.id,)))

def launch(request):
    if not request.session.get('is_login', None):
        return render(request, 'login/login.html', {'error_info': 'Please login first'})

    return render(request, "poll/launch.html", )

def new_topic(request):

    message = 'Failed'

    topic = request.POST['topic']
    type_1 = request.POST['type_of_topic']
    limit_of_voters = request.POST['limit_of_voters']
    launcher = request.session['user_name']


    if request.method == "POST":
        limit = int(request.POST['limit'])
        topic_db = Question(launcher=launcher, question_text=topic, pub_date=datetime.datetime.utcnow().replace(tzinfo=utc), topic=type_1, limit_of_voters=limit_of_voters)
        topic_db.save()

        for i in range(0, limit):
            num = str(i)
            choice = request.POST[num]
            choice_db = Choice(question=topic_db, choice_text=choice)
            choice_db.save()
            message = 'Success'

    return render(request, "poll/Success.html", {'message': message})


def keywords_search(request):
    message = "unreceived"
    if request.method == "POST":
        keywords = request.POST["keywords"]
        if not keywords:
            return render(request, 'poll/index.html', {'message': message})

        global feedback_page
        feedback = Question.objects.filter(question_text__icontains=keywords)
        feedback_page = Paginator(feedback, 7)

    page = request.GET.get('page', '1')
    polls = feedback_page.page(page)

    next_page = 1
    previous_page = 1
    if polls.has_next():
        next_page = polls.next_page_number()
    if polls.has_previous():
        previous_page = polls.previous_page_number()

    poll_number = len(Question.objects.all())
    user_number = len(User.objects.all())

    context = {
        'poll_number': poll_number,
        'user_number': user_number,
        'previous_page': previous_page,
        'next_page': next_page,
        'first_page': 1,
        'last_page': feedback_page.num_pages,
        'polls': polls,

    }
    return render(request, 'poll/index.html', context)


def category(request, name):
    # need a algorithm to order the feedback
    feedback = Question.objects.filter(topic=name).order_by('pub_date')

    # Show 3 contacts per page
    pages = Paginator(feedback, 7)
    # GET method
    page = request.GET.get('page', '1')
    polls = pages.page(page)

    next_page = 1
    previous_page = 1
    if polls.has_next():
        next_page = polls.next_page_number()
    if polls.has_previous():
        previous_page = polls.previous_page_number()

    poll_number = len(Question.objects.all())
    user_number = len(User.objects.all())

    context = {
        'poll_number': poll_number,
        'user_number': user_number,
        'previous_page': previous_page,
        'next_page': next_page,
        'first_page': 1,
        'last_page': pages.num_pages,
        'polls': polls,

    }
    return render(request, 'poll/index.html', context)

def login(request):

    return redirect('/login/')