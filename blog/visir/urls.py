from django.conf.urls import url
from . import views

app_name = 'visir'
urlpatterns = [
    #/history/
    url(r'^$', views.index, name = 'index'),
]