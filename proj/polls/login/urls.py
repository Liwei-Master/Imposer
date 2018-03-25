from django.conf.urls import url
from . import views

app_name = 'login'
urlpatterns = [
        url(r'^$', views.login, name='submit'),
        url(r'^register/$', views.register, name='register'),
        url(r'^logout/$', views.logout, name='logout'),
        url(r'^user_confirm/$', views.user_confirm,),
        url(r'^personal_info/$', views.personal_info, name="personal_info"),
        url(r'^update_info/$', views.update_info, name="update_info"),
        url(r'^send_code/$', views.send_code, name="send_code"),
        url(r'^forget_code/$', views.forget_password, name='forget_password'),

]