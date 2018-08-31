from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context={'insert_me':"Helloo my views.py"}
    return  render(request,'first_app/index.html',context)

# Create your views here.
