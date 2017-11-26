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
	if request.method=='POST':
		userexisted=User.objects.filter(uname=request.POST['username'])
		if len(userexisted)==0:
			newUser=User.objects.create(uname=request.POST['username'],ujob=request.POST['career'],
			uage=request.POST['age'],uemail=request.POST['email'],ucode=request.POST['pswl'],
			ugender=request.POST['gender'])
			newUser.save()
		else:
			return render(request,'booklist/dushubiji.html',{"errors":"用户名已存在"})
		
	return render(request,'booklist/success.html',{'uName':newUser.uname})
def first(request):
	return render(request,'booklist/login3.html')
def login(request):
	if request.method=='POST':
		userlist=User.objects.filter(uname=request.POST['username'],ucode=request.POST['password'])
		if len(userlist)==1:
			user=User.objects.get(uname=request.POST['username'],ucode=request.POST['password'])
			return render(request,'booklist/personal.html',{'username':user.uname})
		else:
			return render(request,'booklist/login3.html',{"errors":"用户名或密码错误"})
    