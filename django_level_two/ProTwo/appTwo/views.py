from django.shortcuts import render
from appTwo.models import User

def index(request):
    return render(request,'appTwo/index.html')

def users(request):
    user_dict={'users':User.objects.order_by('first_name')}
    return  render(request,'appTwo/users.html',user_dict)