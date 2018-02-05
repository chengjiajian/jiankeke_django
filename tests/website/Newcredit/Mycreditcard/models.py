#-*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from mongoengine import *
#from mongoengine import connect

import datetime

connect('UserInfomation', host='127.0.0.1', port=27017)
# Create your models here


##以下填写models

class Messages(Document):
    username = StringField(max_length=255)
    title = StringField(max_length=255)
    content = StringField()
    publish_date = DateTimeField(default=datetime.datetime.now().strftime('%Y-%M-%D'))
    def __str__(self):
        return "{},{},{},{}".format(
            self.username,
            self.title,
            self.content,
            self.publish_date)
    meta = {'db_alias':'test-db'}

class accountDatas(Document):
    userid = IntField(max_length=18)
    username = StringField(max_length=255)
    password = StringField(max_length=255)
    selfIntroduce = StringField(default='',max_length=255)
    phoneNumber = StringField(default='',max_length=11)
    EmailAccount = StringField(default='',max_length=30)
    wechatAccount = StringField(default='',max_length=30)
    weiboAccount = StringField(default='',max_length=30)
    create_date = DateTimeField(default='')
    qqAccount = StringField(default='',max_length=30)
    identifyId = IntField(default=0,max_length=18)
    birthday = DateTimeField(max_length=30,default=datetime.datetime.now(),)
    scores = IntField(default=0)
    region = StringField(default='',max_length=30)
    img = ImageField(default='',upload_to='img')
    meta = {'allow_inheritance': True, 'collection': 'account_datas'}
    def __str__(self):
        return "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}".format(
            self.userid,self.username,self.password,self.selfIntroduce,self.phoneNumber,self.EmailAccount,self.wechatAccount,self.weiboAccount,self.create_date,self.qqAccount,self.identifyId,self.birthday,self.scores,self.region,self.img)

# class superuser(accountDatas):
#     username = StringField(max_length=50)
    # password = StringField(max_length=50)
    # create_date = DateTimeField(blank=True)

# class ZSYH_apply(accountDatas):
#     card_address = StringField(max_length=255,default='')
#     card_name = StringField(max_length=255)
#     pic_address = StringField(max_length=255,default='')
#     def __str__(self):
#         return '{},{},{}'.format(self.card_address,self.card_name,self.pic_address)
# for i in accountDatas.objects[:2]: # 测试是否连接成功
#     print(i.username)