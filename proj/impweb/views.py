from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.views.decorators.csrf import csrf_exempt

import time

from .models import User
from .forms import UserForm

# Create your views here.
'''
def index(request):
    return HttpResponse('Fuck Homepage')
'''

@csrf_exempt
def login (request):
    info='This request is GET'
    if request.method=='POST':
        uf=UserForm(request.POST)
        info='post,not valid%s'%uf.__dict__
        if uf.is_valid():
            username=uf.cleaned_data['username']
            password=uf.cleaned_data['password']


            user=User.objects.filter(username=username,password=password)
            if user:
                #return render(request, "Index.html", {'error_info': "登录成功"})
                return HttpResponse('success!%s,%s'%(username,password))
            else:
                #return render(request, "Login.html", {'error_info': "该用户名或密码不正确，请重新输入"})
                return HttpResponse('该用户名或密码不正确，请重新输入%s,%s'%(username,password))

    #return render(request, "Login.html", {'error_info': "data error,request failed"})
    return HttpResponse('data error, request failed, %s'%info)

@csrf_exempt
def sign_up(request):
    info='This request is GET'
    if request.method == 'POST':
        uf=UserForm(request.POST)
        if uf.is_valid():
            username=uf.cleaned_data['username']
            password=uf.cleaned_data['password']
            #registertime

            newUser= User(username=username,password=password)
            newUser.save()
            #return render(request, "Index.html", {'error_info': "登录成功,听说你是第一次登录哦"})
            return HttpResponse('success')
        else:
            return HttpResponse('not valid')
    #return render(request, "Login.html", {'error_info': "data error,request failed"})
    return HttpResponse('failed,%s'%info)

@csrf_exempt
def reset(request):
    if request.method == 'POST':
        email = str(request.POST.get('send_email'))
        if not email.find("@",2):
            return render(request, "Login.html", {'error_info': "邮箱有误"})

        print(email) # 对比进数据库 是就返回
        return render(request, "PSDchange.html")

@csrf_exempt
def new_passwords(request):

    if request.method == "POST":
        new_password = request.POST.get("new_password")
        print(new_password)# 放进数据库
        return render(request, "Login.html", {'error_info': "密码修改成功！"})
'''
def register(request):
    pass

def login(request):
    error_info='accessable, please login'
    context={'error_info':error_info}
    return render(request,'login.html',context)
'''
def index(request):
    user_list=User.objects.order_by('id')[:5]
    context={'user_list':user_list}
    return render(request,'impweb/index.html',context)

def detail(request,userid):
    user = get_object_or_404(User, pk=userid)
    return render(request, 'impweb/detail.html', {'user': user})
#    return HttpResponse('The userid is %s'%userid)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def test(request, username):
    password='thenull'
    data={'username':username, 'password':password,    'email':'asdfasdfjkjkn@lkl.com',
    'facebook':'lzsjkn'}

    newUser= User(username=username,password=password)
    newUser.save()
    return HttpResponse('failed,%s'%(newUser.__dict__))



