
from django.conf.urls import url
from . import views

app_name = 'history'
urlpatterns = [
    #/history/
    url(r'^$', views.index, name = 'index'),
    #/history/12/
    url(r'^(?P<event_id>[0-9]+)/$', views.detail, name = 'detail'),
    #/history/12/favorite/
    url(r'^(?P<event_id>[0-9]+)/favorite/$', views.favorite, name = 'favorite'),
]
