from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^list_(\d+)_(\d+)_(\d+)/$',views.good_list),
    url(r'^(\d+)/$',views.detail),

]