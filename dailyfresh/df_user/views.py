# coding=utf-8

from django.shortcuts import render,redirect;
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect;
from hashlib import sha1;
from models import UserInfo;
from datetime import *;
import user_decorator;
from df_goods.models import GoodsInfo;
from django.views.decorators.csrf import csrf_exempt;
'''
注册功能
1.用户名是否唯一
2.确认两次密码是否相同
3.密码加密存储

'''


def register(request):
    title = '天天生鲜-注册'
    return render(request, 'df_user/register.html',{'title':title})
# 注册板块


def login(request):
    title = '天天生鲜-登陆'
    return render(request, 'df_user/login.html',{'title':title})
# 登陆板块


def login_out(request):
    request.session.flush()
    return render(request,'df_goods/index.html',{'page_style':0})


def uname_check(request):
    # 获取用户输入uname
    check_uname = request.POST.get('check_uname')
    # 检验数据库中是否有相同uname
    check_result = UserInfo.objects.filter(uname=check_uname).exists()
    # 若数据库中存在则返回True
    return JsonResponse({'check':check_result})
# 用户名验证


def login_check(request):
    post = request.POST
    login_name = post.get("username")
    login_pwd = post.get("pwd")
    # 如果cookie中有‘url’则跳转到之前记录的url,否则跳转到主页
    response = HttpResponseRedirect(request.COOKIES.get('url','/index/'))
    response.delete_cookie('url')
    check_result = UserInfo.objects.filter(uname=login_name).exists()
    if check_result:
        # 对用户输入密码进行加密
        s1 = sha1()
        s1.update(login_pwd)
        login_pwd = s1.hexdigest()

        check_pwd = UserInfo.objects.filter(uname=login_name).values('upwd')[0]['upwd']
        login_id = UserInfo.objects.filter(uname=login_name)[0].id
        # 验证密码是否正确
        if check_pwd == login_pwd:
            post = request.POST
            jizhu = post.get('jizhu')
            if jizhu:
                # cookie未定义时间则关闭浏览器过期
                response.set_cookie('login_name',login_name,None,datetime(2018,1,1))
                print('已经记住密码')
            else:
                response.set_cookie('login_name', '', max_age=-1)
                print('未成功记录密码')

            print('登陆成功')
            # 存储session
            request.session['myname']=login_name
            request.session['id'] = login_id
            # request.session.flush()
            # 获取sessi
            # id = request.session.get('id')
            # 删除session
            # del request.session['myname'],request.session['id']
            return response
        else:
            print('密码错误')
            content = {'title':'用户登陆','error_name':0,'error_pwd':1}
            return render(request,'df_user/login.html',content)
    else:
        response.set_cookie('login_name', '', max_age=-1)
        content = {'title': '用户登陆', 'error_name': 1, 'error_pwd': 0}
        return render(request,'df_user/login.html',content)

    # 相同则登陆页面自动跳转到登陆页面（先判断用户名是否存在）

    # 不同提示账号密码错误
# 登陆验证


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
# 注册验证


@user_decorator.login
def user_center_info(request):
    rec_bro = request.COOKIES.get('goods_ids', '')
    rec_good =[]
    rec_list = rec_bro.split(',')
    if(rec_list !=''):
        for good in rec_list:
            print(good)
            good_obj=GoodsInfo.objects.get(pk=int(good))
            rec_good.append(good_obj)
    return render(request, 'df_user/user_center_info.html',{'page_style':0,'rec_good':rec_good})
# 用户中心