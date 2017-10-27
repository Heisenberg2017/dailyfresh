# coding=utf-8
from django.db import transaction
from django.shortcuts import render, redirect
from df_cars.models import CarInfo
from df_order.models import OrderInfo, OrderDetailInfo
from df_user import user_decorator
from django.http import JsonResponse
from datetime import datetime
from decimal import Decimal
'''
print(oid_obj)时代码报错，原因：？
报错信息：'ascii' codec can't decode byte 0xe8 in position 0: ordinal not in range(128)
引入下面代码解决
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


@user_decorator.login
def order(request):
    carts = request.GET.getlist('cart_id')
    index = range(1, len(carts))
    carts_obj = []
    for cart in carts:
        print('cart:%s' % cart)
        cart_obj = CarInfo.objects.get(pk=int(cart))
        carts_obj.append(cart_obj)
    return render(request, 'df_order/place_order.html', {
        'page_style': 1, 'title': '提交订单', 'carts_obj': carts_obj, 'index': index
    })

# 呈现订单页
@transaction.atomic()
@user_decorator.login
def order_handle(request):
    # 保存一个点
    tran_id = transaction.savepoint()

    cart_ids = str(request.POST.get('cart_ids'))
    total = request.POST.get('total')
    print('cart_ids:%s'%cart_ids)
    print('total:%s' % total)
    try:
        order = OrderInfo()
        now = datetime.now()
        uid = request.session['id']
        # 采用订单创建时间+用户id来表示订单编号
        order.oid = '%s%d' % (now.strftime('%Y%m%d%H%M%S'), uid)
        order.user_id = uid
        order.odate = now
        order.ototal = Decimal(request.POST.get('total'))
        order.save()

        cart_ids1 = [int(item) for item in cart_ids.split(' ')]
        for id1 in cart_ids1:
            detail = OrderDetailInfo()
            # 表示外键order是当前的订单对象
            detail.order = order

            cart = CarInfo.objects.get(id=id1)
            goods = cart.goods
            # 判断库存
            if goods.gkucun >= cart.goods.gkucun:
                goods.gkucun = cart.goods.gkucun - cart.count
                goods.save()

                detail.goods_id = goods.id
                detail.price = goods.gprice
                detail.count = cart.count
                detail.save()

                cart.delete()
            else:
                transaction.savepoint_rollback(tran_id)
                return JsonResponse({'url':'/carts/'})

        transaction.savepoint_commit(tran_id)
    except Exception as e:
        print '===========%s' % e
        transaction.savepoint_rollback(tran_id)

    return JsonResponse({'url':'/user/order_1/'})


@transaction.atomic()
@user_decorator.login
def pay(request):
    # 保存一个点
    err = 0
    tran_id = transaction.savepoint()

    try:
        oid = request.POST.get('oid')
        print ("订单号:%s" % oid)
        oid_obj = OrderInfo.objects.get(oid=int(oid))
        print 1
        print ("oid_obj:%s" % oid_obj)
        oid_obj.oIsPay = True
        print 2
        oid_obj.save()
        print 3
        # 代码执行未出错保存提交
        
        err = 1
        transaction.savepoint_commit(tran_id)
    except Exception as e:
        print '===========%s' % e
        # 代码出错回退到保存点
        transaction.savepoint_rollback(tran_id)

    return JsonResponse({'err': err})