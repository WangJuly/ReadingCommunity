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
		newUser=User.objects.create(uname=request.POST['username'],ujob=request.POST['career'],
		uage=request.POST['age'],uemail=request.POST['email'],ucode=request.POST['pswl'],
		ugender=request.POST['gender'],ulbook=request.POST['book'])
		newUser.save()
	return render(request,'booklist/success.html',{'uName':newUser.uname})
    
    