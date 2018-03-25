from django.shortcuts import render
from django.shortcuts import redirect
from .models import User, ConfirmString
from django.conf import settings
import hashlib
import datetime
import random

from django.core.validators import validate_email
from django.core.exceptions import ValidationError
# Create your views here.

def login(request):
    if request.session.get('is_login', None):
        return redirect('/poll/')
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            name = email.strip()
            user = User.objects.get(email=name)
        except(KeyError, User.DoesNotExist):
            return render(request, 'login/login.html', {'error_info': 'email is incorrect'})

        if hash_code(password) == user.password:

            if not user.has_confirmed:
                return render(request, 'login/login.html', {'error_info': 'The email has not been validated yet '})

            request.session['is_login'] = True
            request.session['user_id'] = user.id
            request.session['user_name'] = user.name
            request.session['email_address'] = user.email

            # more info about redirect in 'https://docs.djangoproject.com/en/2.0/topics/http/shortcuts/'
            return redirect('/poll/')
        else:
            return render(request, 'login/login.html', {'error_info': 'password is incorrect'})

    return render(request, 'login/login.html',)

# form a hash code as the key
def make_confirm_string(user):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user.name, now)
    ConfirmString.objects.create(code=code, user=user,)
    return code

def register(request):
    if request.POST:
        name = request.POST.get('name')
        password = request.POST.get('password')

        sex = request.POST.get('sex')
        if sex != 'Male' and sex != 'Female':
            return render(request, 'login/login.html', {'error_info': 'Sex should be Male or Female'})

        try:
            email = request.POST.get('email')
            validate_email(email)
        except ValidationError:
            return render(request, 'login/login.html', {'error_info': 'Email is not valid '})

        anonymous = User.objects.filter(email=email)
        if anonymous:
            return render(request, 'login/login.html', {'error_info': 'The email you filled in is registered already'})

        anonymous = User.objects.filter(name=name)
        if anonymous:
            return render(request, 'login/login.html', {'error_info': 'The name you filled in is registered already'})

        user = User(name=name, email=email, sex=sex, password=hash_code(password))
        user.save()
        code = make_confirm_string(user)
        send_email(email, code)
        return render(request, 'login/login.html', {'error_info': '请前往注册邮箱，进行邮件确认！'})


    return render(request, 'login/login.html', {'error_info': 'failed'})

def send_email(email, code):

    from django.core.mail import EmailMultiAlternatives

    subject = '欢迎访问Impostor！'

    text_content = '来自Impostor的测试邮件, 欢迎访问Impostor！'

    html_content = '''
                    Welcome to <a href="http://{}/login/user_confirm/?code={}" target=blank>Impostor</a>，
                    来自Impostor的测试邮件, 欢迎访问Impostor！</p>
                    <p>请点击站点链接完成注册确认！</p>
                    <p>此链接有效期为 {} 天！</p>
                    '''.format('127.0.0.1:8000', code, settings.CONFIRM_DAYS)

    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def user_confirm(request):
    code = request.GET.get('code', None)
    message = ''
    try:
        confirm = ConfirmString.objects.get(code=code)
    except:
        message = '无效的确认请求!'
        return render(request, 'login/confirm.html', locals())

    c_time = confirm.c_time

    # datetime.datetime.now is not timezone aware. more info: http://blog.csdn.net/qq_25420115/article/details/53149669
    from django.utils import timezone
    now = timezone.now()
    if now > c_time + datetime.timedelta(settings.CONFIRM_DAYS):
        confirm.user.delete()
        message = '您的邮件已经过期！请重新注册!'
        return render(request, 'login/confirm.html', locals())
    else:
        confirm.user.has_confirmed = True
        confirm.user.save()
        confirm.delete()
        message = '感谢确认，请使用账户登录！'
        return render(request, 'login/confirm.html', locals())


def logout(request):
    if request.session.get('is_login', None):
        request.session.flush()

    return redirect("/poll/")


code = int(random.random() * 1000000)
code_email = ""


def send_code(request):
    message = "Failed"
    if request.POST:
        global code_email
        try:
            code_email = request.POST.get('email')
            validate_email(code_email)
        except ValidationError:
            return render(request, 'login/login.html', {'error_info': 'Email is not valid '})

        global code
        code = int(random.random() * 1000000)

        from django.core.mail import EmailMultiAlternatives
        subject = 'New password from Impostor！'
        text_content = 'Email form Impostor, Your code is ' + str(code) + '!'
        msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [code_email])
        msg.send()
        message = "Email has been sent "

    return render(request, 'login/login.html', {'error_info': message})


def forget_password(request):
    error_info = "Failed"
    if request.POST:
        check_code = request.POST.get('code')
        if not check_code:
            error_info = "No code received"

        else:
            if code == int(check_code):
                password = request.POST.get('password')
                if len(password) < 6:
                    error_info = "the password is too short"

                else:
                    user = User.objects.get(email=code_email)
                    user.password = hash_code(password)
                    user.save()
                    error_info = 'Password has been reset'
            else:
                error_info = 'The code is incorrect'
    return render(request, 'login/login.html', {'error_info': error_info})


def hash_code(s, salt='mysite'):# 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()


def personal_info(request):
    name = request.session['user_name']
    email = request.session['email_address']

    return render(request, 'login/personal_Info.html', {'name': name, 'email': email})


def update_info(request):
    message = "Failed"

    if request.method == "POST":
        user_email = request.session['email_address']
        user = User.objects.get(email=user_email)

        password_1 = request.POST.get('password')
        password_2 = request.POST.get('new_password')
        if password_1 != password_2:
            message = "The passwords should be same."
            return render(request, 'login/personal_Info.html', {'message': message})
        elif password_1:
            new_password = hash_code(password_1)
            user.password = new_password

        name = request.POST.get('name')
        if name != user.name:
            user.name = name

        user.save()
        message = 'Changes have been updated'

        return render(request, 'login/personal_Info.html', {'name': user.name, 'email': user.email, 'message': message})

    return render(request, 'login/personal_Info.html', {'message': message})