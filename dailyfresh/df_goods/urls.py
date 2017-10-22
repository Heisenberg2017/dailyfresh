from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^list_(\d+)_(\d+)_(\d+)/$',views.list),
    url(r'^list_\d+_\d+_\d+/(\d+)$',views.detail),

]