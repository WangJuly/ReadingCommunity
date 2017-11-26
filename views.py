# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from booklist.models import *
##def index(request):
	##return HttpResponse(u"123")
##def index(request):
	##tutorlist=["ab","bgg","cff","ds","esaw"]
	##return render(request, 'booklist/dushu.html',{'tutorlist':tutorlist})
def index(request):
	return render(request,'booklist/dushubiji.html')
def getUser(request):
	User.objects.create(uname=request.GET['username'],ujob=request.GET['career'],
		uage=request.GET['age'],uemail=request.GET['email'],ucode=request.GET['pswl'],
		ugender=request.GET['gender'],ulbook=request.GET['book'])
def article(request):
	return render(request,'booklist/upload.html')
def getArticle(request):
	Article.objects.create(atitle=request.GET['atitle'],abookname=request.GET['abookname'],awriter=request.GET['awriter'],acontent=request.GET['acontent'])
	return render(request,'booklist/uploadsuccess.html')
def personal(request):
        return render(request,'booklist/personal.html')
def personalarticle(request):
        personalarticle = Article.objects.filter(aauthor="zhengsiqi")
        return render(request,'booklist/personalarticle.html',{'personalarticle':personalarticle})
        
#Userdesign.save()
    
