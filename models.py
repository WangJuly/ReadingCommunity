from django.db import models

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

class Article(models.Model):
    atitle=models.CharField(u'笔记标题',max_length=30)
    aauthor=models.CharField(u'笔记作者',max_length=30)
    abookname=models.CharField(u'书籍名称',max_length=30)
    awriter=models.CharField(u'书籍作者',max_length=30)
    acontent=models.TextField(u'笔记正文',max_length=10000)
    def __str__(self):
        return self.atitle

class Star(models.Model):
    suname=models.CharField(u'收藏用户',max_length=50)
    stitle=models.CharField(u'收藏笔记的标题',max_length=30)
    #sauthor=models.CharField(u'收藏笔记的作者',max_length=30)
    #sbookname=models.CharField(u'收藏笔记的书籍名称',max_length=30)
    #swriter=models.CharField(u'收藏笔记的书籍作者',max_length=30)
    #scontent=models.TextField(u'收藏笔记的正文',max_length=10000)

    def __str__(self):
        return self.suname
		
class StarUser(models.Model):
        starusername=models.CharField(u'收藏用户',max_length=50)
        staruserauthor=models.CharField(u'收藏者',max_length=50)
        def __str__(self):
            return self.staruserauthor
