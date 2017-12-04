from django.shortcuts import redirect
from django.http import HttpResponseRedirect


def login(func):
    """验证用户登陆装饰器"""
    def login_fun(request, *args, **kwargs):
        if request.session.has_key('id'):
            return func(request, *args, **kwargs)
        else:
            red = HttpResponseRedirect('/user/login')
            red.set_cookie('url', request.get_full_path())
            return red
    return login_fun
