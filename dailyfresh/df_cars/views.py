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
        cart.count += count
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


def edit(request,cart_id,count):
    print('cart_id:%s'%cart_id)
    print('count:%s' % count)
    try:
        cart=CarInfo.objects.get(pk=int(cart_id))
        count1 = cart.count=int(count)
        cart.save()
        data = {'ok': 1}
    except Exception as e:
        data={'ok':count1}
    return JsonResponse(data)


def delete(request,cart_id):
    try:
        cart=CarInfo.objects.get(pk=int(cart_id))
        cart.delete()
        data={'ok':1}
    except Exception as e:
        data={'ok':0}
    return JsonResponse(data)