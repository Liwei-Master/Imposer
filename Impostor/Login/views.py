from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

# 根据API 返回 内容
username_list = ("Tony", "Wang")
keywords_list = ("123")

def Login (request):

    return render(request, "Login.html", {'error_info': "是第一次的话，请申请账号"})

def submit (request):
    username = request.POST['username'].strip()
    keywords = request.POST['keywords'].strip()

    if request.method == 'POST' and username in username_list:

        print(username, keywords)

        if keywords in keywords_list:

            return render(request, "Login.html", {'error_info': "登陆成功"})
        else:
            return render(request, "Login.html", {'error_info': "该用户名或密码不正确，请重新输入"})

    else:
        return render(request, "Login.html", {'error_info': "是第一次的话，请申请账号"})




