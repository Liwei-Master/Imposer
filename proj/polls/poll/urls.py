from django.conf.urls import url
from . import views


app_name = 'poll' #app name of the urls
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^launch/$', views.launch, name='launch'),
    url(r'^search/$', views.keywords_search, name='search'),
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /poll/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^category/(?P<name>[A-Za-z]+)/$', views.category, name="category"),
    url(r'^login/$', views.login, name='login'),
]