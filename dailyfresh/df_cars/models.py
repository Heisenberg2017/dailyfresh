from django.db import models


class CarInfo(models.Model):
    """购物车信息"""
    user = models.ForeignKey('df_user.UserInfo')
    goods = models.ForeignKey('df_goods.GoodsInfo')
    count = models.IntegerField()