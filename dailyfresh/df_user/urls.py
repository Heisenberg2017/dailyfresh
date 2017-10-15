from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
    url(r'^index/$', views.index),
    url(r'^register_handle/$', views.register_handle),
    url(r'^uname_check/$', views.uname_check),
]