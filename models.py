from django.db import models
# -*- coding: utf-8 -*-
# Create your models here.

class User(models.Model):
	uname=models.CharField(max_length=50)
	ugender=models.CharField(max_length=50,default='female')
	uage=models.IntegerField()
	ucode=models.CharField(max_length=50)
	uemail=models.EmailField(max_length=254)
	ujob=models.CharField(max_length=10)
	ulbook=models.CharField(max_length=200,default='None')
	uarticlenumber=models.IntegerField(default=0)
	def __str__(self):
		return self.uname

class Article(models.Model):
    atitle=models.CharField(u'笔记标题',max_length=30)
    aauthor=models.CharField(u'笔记作者',max_length=30)
    abookname=models.CharField(u'书籍名称',max_length=30)
    awriter=models.CharField(u'书籍作者',max_length=30)
    acontent=models.TextField(u'笔记正文',max_length=10000)
    def __str__(self):
        return self.atitle