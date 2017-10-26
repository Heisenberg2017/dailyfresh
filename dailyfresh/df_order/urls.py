from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.order),
    url(r'^order_handle/$', views.order_handle),

]