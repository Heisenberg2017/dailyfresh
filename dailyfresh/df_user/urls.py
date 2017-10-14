from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^register/$', views.register)
]