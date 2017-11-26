# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from booklist.models import *
@csrf_exempt
##def index(request):
	##return HttpResponse(u"123")
##def index(request):
	##tutorlist=["ab","bgg","cff","ds","esaw"]
	##return render(request, 'booklist/dushu.html',{'tutorlist':tutorlist})
def index(request):
        return render(request,'booklist/register.html')
def getUser(request):
        if request.method=='POST':
                userexisted=User.objects.filter(uname=request.POST['username'])
                if len(userexisted)==0:
                        newUser=User.objects.create(uname=request.POST['username'],ujob=request.POST['career'],
                        uage=request.POST['age'],uemail=request.POST['email'],ucode=request.POST['pswl'],
                        ugender=request.POST['gender'])
                        newUser.save()
                else:
                        return render(request,'booklist/register.html',{"errors":"用户名已存在"})
        return render(request,'booklist/registersuccess.html',{'uName':newUser.uname})
def first(request):
        return render(request,'booklist/login.html')
def login(request):
        if request.method=='POST':
                userlist=User.objects.filter(uname=request.POST['username'],ucode=request.POST['password'])
                if len(userlist)==1:
                        user=User.objects.get(uname=request.POST['username'],ucode=request.POST['password'])
                        request.session['username']=user.uname
                        return render(request,'booklist/personal.html',{'username':user.uname})
                else:
                        return render(request,'booklist/login.html',{"errors":"用户名或密码错误"})
   
def article(request):
        return render(request,'booklist/upload.html')
def getArticle(request):
        username=request.session.get('username')
        Article.objects.create(atitle=request.GET['atitle'],abookname=request.GET['abookname'],awriter=request.GET['awriter'],acontent=request.GET['acontent'],aauthor=username)
        return render(request,'booklist/uploadsuccess.html')
def personal(request):
        username = request.session.get('username')
        return render(request,'booklist/personal.html',{'username':username})
def personalarticle(request):
        username=request.session.get('username')
        personalarticle = Article.objects.filter(aauthor=username)
        personallength=len(personalarticle)
        return render(request,'booklist/personalarticle.html',{'personalarticle':personalarticle,'personallength':personallength})
def personalcontent(request):
        personalcontent = Article.objects.get(atitle=request.GET['id'])
        request.session['title']=personalcontent.atitle
        return render(request,'booklist/personalcontent.html',{'personalcontent':personalcontent})
def stararticle(request):
        stararticle = Article.objects.filter(aauthor=request.GET['username'])
        text2=stararticle[0]
        starlength=len(stararticle)
        return render(request,'booklist/stararticle.html',{'stararticle':stararticle,'starlength':starlength,'text2':text2})
def starcontent(request):
        starcontent = Article.objects.get(atitle=request.GET['id'])
        return render(request,'booklist/starcontent.html',{'starcontent':starcontent})
def bookarticle(request):
        bookarticle = Article.objects.filter(abookname=request.GET["bbookname"])
        namewriter = bookarticle[0]
        return render(request,'booklist/bookarticle.html',{'bookarticle':bookarticle, 'namewriter':namewriter})
def searchcontent(request):
        searchcontent = Article.objects.get(atitle=request.GET['id'])
        return render(request,'booklist/searchcontent.html',{'searchcontent':searchcontent})
def delarticle(request):
        aimtitle=request.session.get('title')
        article=Article.objects.get(atitle=aimtitle)
        article.delete()
        username=request.session.get('username')
        personalarticle = Article.objects.filter(aauthor=username)  
        personallength=len(personalarticle)     
        return render(request,'booklist/personalarticle.html',{'personalarticle':personalarticle,'personallength':personallength})

     
#Userdesign.save()
    
