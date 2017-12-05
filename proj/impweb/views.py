from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404

from .models import User

# Create your views here.
'''
def index(request):
    return HttpResponse('Fuck Homepage')
'''
def register(request):
    pass

def login(request):
    error_info='accessable, please login'
    context={'error_info':error_info}
    return render(request,'login.html',context)

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



