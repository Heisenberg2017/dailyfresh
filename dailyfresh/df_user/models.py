from django.db import models


class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30)
    ushou = models.CharField(max_length=20)
    uaddress = models.CharField(max_length=100)
    uyoubian = models.CharField(max_length=6)
    yphone = models.CharField(max_length=11)
