# coding=utf-8
from django.shortcuts import render
from df_cars.models import CarInfo


def order(request):
    return render(request,'df_order/place_order.html',{'page_style':1,'title':'提交订单'})

# 呈现订单页
def order_handle(request):
    carts = request.GET.getlist('cart_id')
    index = range(1,len(carts))
    carts_obj = []
    for cart in carts:
        print('cart:%s'%cart)
        cart_obj = CarInfo.objects.get(pk=int(cart))
        carts_obj.append(cart_obj)
    return render(request,'df_order/place_order.html',{
        'page_style':1,'title':'提交订单','carts_obj':carts_obj,'index':index
    })