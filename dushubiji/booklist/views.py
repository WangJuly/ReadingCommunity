# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
#from django.contrib import auth
#from django import forms
#from django.template import RequestContext
from booklist.models import *
def index(request):
	return render(request,'booklist/dushubiji.html')
def getUser(request):
	if request.method=="POST":
	    User.objects.create(uname=request.POST['username'],ujob=request.POST['career'],
		uage=request.POST['age'],uemail=request.POST['email'],ucode=request.POST['pswl'],
		ugender=request.POST['gender'],ulbook=request.POST['book'])
	return HttpResponse(u"you success")
	#return redener(request,'booklist/success.html')
    