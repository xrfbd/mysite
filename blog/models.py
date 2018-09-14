# coding=utf-8

from __future__ import unicode_literals
# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Article(models.Model):
    title=models.CharField(u'标题',max_length=50)
    content=models.CharField(u'正文',max_length=3000)
    date = models.DateTimeField(u'创建日期', null=True)
    like = models.IntegerField(u'点赞',null=True)
    reading = models.IntegerField(u'阅读量', null=True)
    labels=models.ManyToManyField('Label')
    def __unicode__(self):
        return self.title

class Label(models.Model):
    label=models.CharField(u'标签',max_length=10,null=True)
    articles=models.ManyToManyField(Article)
    def __unicode__(self):
        return self.label


#class User(models.Model):
 #   username = models.CharField(u'标签', max_length=12)
 #   password = models.CharField(u'标签', max_length=12)
 #   def __unicode__(self):
 #       return self.username


#档案:扩展auth用户信息，调用user.get_profile()函数来获得用户档案
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    realname = models.CharField(max_length=16, default='', null=False)
    email = models.EmailField(max_length=100, null=True)
    phone = models.IntegerField(max_length=11, null=True)
    def __unicode__(self):
        return self.realname