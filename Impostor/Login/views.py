from django.shortcuts import render
from django.shortcuts import HttpResponse
import json

# Create your views here.
# test command : python manage.py runserver 127.0.0.1:8000
# 根据API 返回 内容
username_list = ("Tony", "Wang")
keywords_list = ("123")

def Login (request):

    return render(request, "Login.html", {'error_info': "是第一次的话，请申请账号"})

def submit (request):
    username = request.POST.get('email')
    keywords = request.POST.get('keywords')

    if request.method == 'POST' and username in username_list: # 对比数据库

        print(username, keywords)

        if keywords in keywords_list: # 对比数据库

            return render(request, "Index.html", {'error_info': "登陆成功"})
        else:
            return render(request, "Login.html", {'error_info': "该用户名或密码不正确，请重新输入"})

    else:
        return render(request, "Login.html", {'error_info': "是第一次的话，请申请账号"})

def sign_up(request):

    if request.method == 'POST':
        email = request.POST.get('set_email')
        keywords = request.POST.get('set_password')
        username = request.POST.get('set_name')

        print(email, keywords, username) # 放进数据库
        return render(request, "Login.html", {'error_info': "听说你是第一次登录哦"})

def reset(request):
    if request.method == 'POST':
        email = str(request.POST.get('send_email'))
        if not email.find("@",2):
            return render(request, "Login.html", {'error_info': "邮箱有误"})

        print(email) # 对比进数据库 是就返回
        return render(request, "PSDchange.html")

def new_passwords(request):

    if request.method == "POST":
        new_password = request.POST.get("new_password")
        print(new_password)# 放进数据库
        return render(request, "Login.html", {'error_info': "密码修改成功！"})

#def sign_up (request):
 #   json_data = request.POST.get('data')
  #  content = json.loads(json_data)

   # email = content[0].new_email
    #keyword = content[1].keywords
    #name = content[2].name

    #print(email, keyword, name)


    #return render(request, "Login.html", {'error_info': "听说你是第一次登录哦"})


