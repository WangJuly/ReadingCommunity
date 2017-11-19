from django.db import models
# -*- coding: utf-8 -*-
# Create your models here.
class Book(models.Model):
	btitle=models.CharField(u'标题',max_length=100)
	btutor=models.CharField(u'作者',max_length=50)
	def __str__(self):
		return self.btitle

class User(models.Model):
	uname=models.CharField(max_length=50)
	ugender=models.CharField(max_length=50,default='female')
	uage=models.IntegerField()
	ucode=models.CharField(max_length=50)
	uemail=models.EmailField(max_length=254)
	ujob=models.CharField(max_length=10)
	ulbook=models.CharField(max_length=200,default='None')
	def __str__(self):
		return self.uname
