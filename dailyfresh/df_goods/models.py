# coding=utf-8
from django.db import models
from tinymce.models import HTMLField


class TypeInfo(models.Model):
    # 商品类型
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)


class GoodsInfo(models.Model):
    # 商品信息
    gtitle = models.CharField(max_length=20)
    gpic = models.ImageField(upload_to='df_goods')
    gprice = models.DecimalField(max_digits=5,decimal_places=2)
    isDelete = models.BooleanField(default = False)
    gunit = models.CharField(max_length=20,default='500g')
    gclick = models.IntegerField()
    gjanjie = models.CharField(max_length=200)
    gkucun = models.IntegerField()
    gcontent = HTMLField()
    gtype = models.ForeignKey(TypeInfo)