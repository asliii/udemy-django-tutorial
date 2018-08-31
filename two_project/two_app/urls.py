from django.conf.urls import url
from two_app import views

urlpatterns = [
    url(r'^$',views.help,name='index')
]