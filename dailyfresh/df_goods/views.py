# coding=utf-8
from django.shortcuts import render
from models import TypeInfo,GoodsInfo
from django.core.paginator import *


def index(request):
    # 记录登陆状态
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


def list(request, tid, pindex, sort):
    # 最新的两条goods
    typeinfo = TypeInfo.objects.get(pk=int(tid))
    news = typeinfo.goodsinfo_set.order_by('-id')[0:2]

    # goods排序
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
    return render(request,'df_goods/detail.html',{'page_style': 1})

