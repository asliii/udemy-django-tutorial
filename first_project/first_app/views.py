from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import WebPage, AccessRecord, Topic

def index(request):
    context={'acc_rec':AccessRecord.objects.order_by('date')}
    return  render(request,'first_app/index.html',context)

# Create your views here.
