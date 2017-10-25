from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.carts),
    url(r'^(\d+)_(\d+)/$', views.add),
    url(r'^edit_(\d+)_(\d+)/$', views.edit),
    url(r'^delete_(\d+)/$', views.delete),
]