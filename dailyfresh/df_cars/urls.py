from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.carts),
    url(r'^(\d+)_(\d+)/$', views.add),
]