
from django.conf.urls import url
from . import views

urlpatterns = [
    #/history/
    url(r'^$', views.index, name = 'index'),
    #/history/12/
    url(r'^(?P<event_id>[0-9]+)/$', views.detail, name = 'detail')
]
