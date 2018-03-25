import os
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'polls.settings'

if __name__ == '__main__':
    subject, from_email, to = '欢迎访问Impostor！', 'heliwei19950119@gmail.com', '296390818@qq.com'
    text_content = '来自Impostor的测试邮件, 欢迎访问Impostor！'
    html_content = '<p>Welcome to<a href="http://www.baidu.com" target=blank>Impostor</a>，来自Impostor的测试邮件, 欢迎访问Impostor！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

