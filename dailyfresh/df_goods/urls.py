from django.conf.urls import include, url
import views
from views import *

urlpatterns = [
    url(r'^$', views.index),
    url(r'^list_(\d+)_(\d+)_(\d+)/$', views.good_list),
    url(r'^(\d+)/$', views.detail),
    url(r'^search/', MySearchView()),
]