# coding=utf-8
from django.shortcuts import render,redirect
from models import *
from django.http import JsonResponse


def carts(request):

    uid = request.session['id']
    cart = CarInfo.objects.filter(user_id=uid)
    context={'title': '购物车', 'page_style': 1, 'cart': cart}

    return render(request,'df_carts/cart.html',context)


def add(request, gid, count):
    uid = request.session['id']
    gid = int(gid)
    count = int(count)
    print('uid:%s'%uid)
    print('gid:%s'%gid)
    print('count:%s'%count)

    carts = CarInfo.objects.filter(user_id=uid, goods_id=gid)
    if len(carts) >= 1:
        cart = carts[0]
        cart.count = cart.count + count
    else:
        cart = CarInfo()
        cart.user_id = uid
        cart.goods_id = gid
        cart.count = count
    cart.save()

    if request.is_ajax():
        count = CarInfo.objects.filter(user_id=request.session['id']).count()
        return JsonResponse({'count': count})
    else:
        return redirect('/carts/')