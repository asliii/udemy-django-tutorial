from django.shortcuts import render
#from appTwo.models import User
from appTwo.forms import NewUserForm

def index(request):
    return render(request,'appTwo/index.html')

def users(request):
    form = NewUserForm()
    if  request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print ('lütfen formu eksiksiz doldurun!')
    return  render(request,'appTwo/users.html',{'form':form})