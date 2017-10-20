# coding=utf-8
from django.shortcuts import render


# 测试用搜索栏模板


def base_search(request):
    # page_style=0页面搜索框为主页的显示风格,page_style=1页面搜索框为用户中心
    return render(request, 'base_search.html',{'page_style': 1})




