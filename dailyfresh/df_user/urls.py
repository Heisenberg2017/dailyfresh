from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
    url(r'^login_out/$', views.login_out),
    url(r'^register/register_handle/$', views.register_handle),
    url(r'^register/uname_check/$', views.uname_check),
    url(r'^login/login_check/$', views.login_check),
    url(r'^user_center_info/$', views.user_center_info),
    url(r'^order_(\d+)/$', views.user_center_order),

]