from django.shortcuts import render

def index(request):
    context={'text':'My name is Asli','istenmeyen':'beni değil onu kes'}
    return render(request,'basicap/index.html',context)
def other(request):
    return render(request,'basicap/other.html')
def relative(request):
    return render(request,'basicap/relative_url_templates.html')