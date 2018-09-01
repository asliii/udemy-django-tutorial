from django.conf.urls import url
from basicap import views

app_name = 'basicap'

urlpatterns = [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other')
]