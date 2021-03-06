# coding=utf-8
from django.shortcuts import render

from df_cars.models import CarInfo
from models import TypeInfo,GoodsInfo
from django.core.paginator import *
from django.http import HttpResponse
from haystack.views import SearchView


def index(request):
    """首页""" 
    myname = request.session.get('myname')
    id = request.session.get('id')

    typelist = TypeInfo.objects.all()

    type0 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type01 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    type1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    type2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
    type3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]
    type4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]
    type5 = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    type51 = typelist[5].goodsinfo_set.order_by('-gclick')[0:4]
    return render(request, 'df_goods/index.html',{
        'myname':myname,'id':id,'page_style':0,
        'type0':type0,'type01':type01,
        'type1': type1, 'type11': type11,
        'type2': type2, 'type21': type21,
        'type3': type3, 'type31': type31,
        'type4': type4, 'type41': type41,
        'type5': type5, 'type51': type51,
    })


def good_list(request, tid, pindex, sort):
    """商品列表页"""
    # 筛选最新的两条商品信息用于展示
    typeinfo = TypeInfo.objects.get(pk=int(tid))
    news = typeinfo.goodsinfo_set.order_by('-id')[0:2]

    # 商品列表排序
    if sort == '1':
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')
    elif sort == '2':
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gprice')
    elif sort == '3':
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gclick')

    # 分页对象
    paginator = Paginator(goods_list,'3')
    page = paginator.page(pindex)
    content={
        'typeinfo':typeinfo,
        'news':news,
        'goods_list':goods_list,
        'page':page,
        'sort':sort,
        'page_style': 1,
    }
    return render(request,'df_goods/list.html',content)


def detail(request,gid):
    """商品详情页"""
    good = GoodsInfo.objects.get(pk=int(gid))
    typeinfo = TypeInfo.objects.get(pk=int(good.gtype_id))
    news = typeinfo.goodsinfo_set.order_by('-id')[0:2]
    # 记录用户点击动作
    good.gclick += 1
    good.save()

    response = render(request, 'df_goods/detail.html', {
        'page_style': 0,
        'good': good,
        'news': news,
    })
    # 最近浏览
    goods_ids = request.COOKIES.get('goods_ids', '')
    good_id = '%d' % good.id
    if goods_ids != '':
        goods_ids1 = goods_ids.split(',')
        if goods_ids1.count(good_id) >= 1:
            goods_ids1.remove(good_id)
        if len(goods_ids1) >= 5:
            del goods_ids1[0]
        goods_ids1.insert(0,good_id)
        goods_ids = ','.join(goods_ids1)
    else:
        goods_ids = good_id

    response.set_cookie('goods_ids', goods_ids)
    return response


def cart_count(request):
    """返回购物车内的商品数目"""
    if request.session.has_key('user_id'):
        return CarInfo.object.filter(user_id = request.session['id'])
    else:
        return 0


class MySearchView(SearchView):
    """搜索结果展示页"""
    def extra_context(self):
        context = super(MySearchView, self).extra_context()
        context['title'] = '搜索'
        context['page_style'] = 1
        context['cart_count'] = cart_count(self.request)
        return context