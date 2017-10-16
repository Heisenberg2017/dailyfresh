# coding=utf-8

from django.shortcuts import render,redirect;
from django.http import HttpResponse,JsonResponse;
from hashlib import sha1;
from models import UserInfo;
from django.views.decorators.csrf import csrf_exempt
'''
注册功能
1.用户名是否唯一
2.确认两次密码是否相同
3.密码加密存储

'''


def index(request):
    return render(request, 'df_user/index.html')


def register(request):
    title = '天天生鲜-注册'
    return render(request, 'df_user/register.html',{'title':title})


def login(request):
    title = '天天生鲜-登陆'
    return render(request, 'df_user/login.html',{'title':title})


def uname_check(request):
    # 获取用户输入uname
    check_uname = request.POST.get('check_uname')
    # 检验数据库中是否有相同uname
    check_result = UserInfo.objects.filter(uname=check_uname).exists()
    # 若数据库中存在则返回True
    return JsonResponse({'check':check_result})


def register_handle(request):
    # 获取注册信息
    post = request.POST
    uname = post.get('user_name')
    upwd1 = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')
    # 验证两次密码是否相同
    if upwd1 == upwd2:
        # 密码加密
        s1 = sha1()
        s1.update(upwd1)
        upwd3 = s1.hexdigest()

        #存入数据库
        user = UserInfo()
        user.uname = uname
        user.upwd = upwd3
        user.uemail = uemail
        user.save()

        return redirect('/user/login/')

    else:
        return redirect('/user/register/')
    return HttpResponse('<script>alert("注册成功")</script>')