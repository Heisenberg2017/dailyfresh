# coding=utf-8
from django.shortcuts import render,redirect
from df_user import user_decorator
from models import *
from django.http import JsonResponse


@user_decorator.login
def carts(request):
    """购物车页"""
    uid = request.session['id']
    cart = CarInfo.objects.filter(user_id=uid)
    context={'title': '购物车', 'page_style': 1, 'cart': cart}

    return render(request,'df_carts/cart.html',context)


def add(request, gid, count):
    """根据传入商品id及数量,修改购物车信息"""
    uid = request.session['id']
    gid = int(gid)
    count = int(count)
    print('uid:%s'%uid)
    print('gid:%s'%gid)
    print('count:%s'%count)
    # 由商品id及数量查询该商品
    carts = CarInfo.objects.filter(user_id=uid, goods_id=gid)
    # 购物车有此商品.更新商品数量
    if len(carts) >= 1:
        cart = carts[0]
        cart.count += count
    # 购物车没有此商品,创建一个购物车信息的实例,添加商品信息
    else:
        cart = CarInfo()
        cart.user_id = uid
        cart.goods_id = gid
        cart.count = count
    cart.save()
    # 如果为ajax异步请求,返回带有商品数量的json数据
    if request.is_ajax():
        # 以下代码更改成count = cart.count
        count = CarInfo.objects.filter(user_id=request.session['id']).count()
        return JsonResponse({'count': count})
    # 请求来自get方式,跳转到购物车页面
    else:
        return redirect('/carts/')


def edit(request,cart_id,count):
    """根据购物车id,修改购物车对象对应商品数目"""
    print('cart_id:%s'%cart_id)
    print('count:%s' % count)
    try:
        cart=CarInfo.objects.get(pk=int(cart_id))
        count1 = cart.count=int(count)
        cart.save()
        data = {'ok': 0}
    except Exception as e:
        data={'ok':count1}
    return JsonResponse(data)


def delete(request,cart_id):
    """根据购物车id,删除购物车对象对应商品"""
    print('cart_id:%s' % cart_id)
    try:
        cart=CarInfo.objects.get(pk=int(cart_id))
        cart.delete()
        data={'ok':1,'cart_id':cart_id}
    except Exception as e:
        data={'ok':0}
    return JsonResponse(data)