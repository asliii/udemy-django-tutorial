from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<strong>Hello World :)</strong>')

def help(request):
    my_help = {'help_insert':"404 Not found :D"}
    return  render(request,'two_app/help.html',my_help)
