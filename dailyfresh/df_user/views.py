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

# 登陆验证
def login_check(request):
    post = request.POST
    login_name = post.get("username")
    login_pwd = post.get("pwd")
    # 判断是否与数据库中相同
    check_result = UserInfo.objects.filter(uname=login_name).exists()
    if check_result:
        # 对用户输入密码进行加密
        s1 = sha1()
        s1.update(login_pwd)
        login_pwd = s1.hexdigest()

        check_pwd = UserInfo.objects.filter(uname=login_name).values('upwd')[0]['upwd']
        # 验证密码是否正确
        if check_pwd == login_pwd:
            print('登陆成功')
            request.session['myname']=login_name
            return redirect('/user/index/')
        # request.session['myname']
        else:
            print('密码错误')
            # 用seeion
    else:
        print('用户名错误')


    return HttpResponse('<script>alert(%s);alert(%s)</script>'%(login_name,login_pwd))
    # 相同则登陆页面自动跳转到登陆页面（先判断用户名是否存在）

    # 不同提示账号密码错误

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