# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from booklist.models import *
@csrf_exempt


#注册界面
def index(request):
        return render(request,'booklist/register.html')
#注册函数
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
#登录界面
def first(request):
        return render(request,'booklist/login.html')
#登录函数
def login(request):
        if request.method=='POST':
                userlist=User.objects.filter(uname=request.POST['username'],ucode=request.POST['password'])
                if len(userlist)==1:
                        user=User.objects.get(uname=request.POST['username'],ucode=request.POST['password'])
                        request.session['username']=user.uname
                        user1=User.objects.get(uname=user.uname)
                        return render(request,'booklist/personal.html',{'username':user.uname,'user1':user1})
                else:
                        return render(request,'booklist/login.html',{"errors":"用户名或密码错误"})
   

#个人界面
def personal(request):
        username = request.session.get('username')
        user1=User.objects.get(uname=username)      #将当前用户存入session
        return render(request,'booklist/personal.html',{'username':username,'user1':user1})
 


#个人笔记
def personalarticle(request):
        username=request.session.get('username')
        personalarticle = Article.objects.filter(aauthor=username)     #当前用户笔记的列表
        personallength = len(personalarticle)                          #当前用户笔记的列表长度
        return render(request,'booklist/personalarticle.html',{'personalarticle':personalarticle,'personallength':personallength})
def personalcontent(request):
        personalcontent = Article.objects.get(atitle=request.GET['id'])     #获取当前用户笔记的某一标题
        request.session['title']=personalcontent.atitle                     #将这一标题存入session的title中
        return render(request,'booklist/personalcontent.html',{'personalcontent':personalcontent})
def delarticle(request):
        aimtitle=request.session.get('title')
        article=Article.objects.get(atitle=aimtitle)
        article.delete()
        username=request.session.get('username')
        personalarticle = Article.objects.filter(aauthor=username)  
        personallength=len(personalarticle)     
        return render(request,'booklist/personalarticle.html',{'personalarticle':personalarticle,'personallength':personallength})



#收藏的笔记
def stararticle(request):
        username=request.session.get('username')
        stararticle = []              #存放Article的列表
        stararticle1 = Star.objects.filter(suname=username)      #当前用户收藏的笔记列表
        for i in stararticle1:
                tem = Article.objects.get(atitle = i.stitle)     #通过收藏笔记的标题获得Article对象
                stararticle.append(tem)                          #将Article对象添加到Article列表中
        starlength=len(stararticle)
        return render(request,'booklist/stararticle.html',{'stararticle':stararticle,'starlength':starlength})
def starcontent(request):
        starcontent = Article.objects.get(atitle=request.GET['id'])
        request.session['startitle']=starcontent.atitle
        return render(request,'booklist/starcontent.html',{'starcontent':starcontent})
def delstar(request):
        aimstartitle=request.session.get('startitle')
        username=request.session.get('username')
        article=Star.objects.get(stitle=aimstartitle,suname=username)
        article.delete()
        stararticle = []
        stararticle1 = Star.objects.filter(suname=username)
        for i in stararticle1:
                tem = Article.objects.get(atitle = i.stitle)
                stararticle.append(tem)
        starlength=len(stararticle)
        return render(request,'booklist/stararticle.html',{'stararticle':stararticle,'starlength':starlength})
def delstaruser(request):
        newstaruser=[]
        aimusername=request.session.get('aimusername')
        nowuser=request.session.get('username')
        aimuser=StarUser.objects.get(starusername=aimusername,staruserauthor=nowuser)
        aimuser.delete()
        staruser1=StarUser.objects.filter(staruserauthor=nowuser)
        for i in staruser1:
                tem = User.objects.get(uname = i.starusername)
                newstaruser.append(tem)
        starlength = len(newstaruser)
        return render(request,'booklist/staruser.html',{'staruser':newstaruser,'starlength':starlength})
def searchstar(request):
        username=request.session.get('username')
        startitle=request.session.get('startitle')
        starexisted = Star.objects.filter(suname=username,stitle=startitle)
        if len(starexisted) == 0:
                Star.objects.create(suname=username,stitle=startitle)
                abookname = request.session.get('bookname')
                bookarticle = Article.objects.filter(abookname=abookname)
                booklength=len(bookarticle)
                return render(request,'booklist/bookarticle.html',{'bookarticle':bookarticle,'booklength':booklength})
        else:
                searchcontent=Article.objects.get(atitle=startitle)
                return render(request,'booklist/searchcontent.html',{'searchcontent':searchcontent,'errors':'您已收藏过该笔记'})
def otherstar(request):
        username=request.session.get('username')
        startitle=request.session.get('startitle')
        othername=request.session.get('othername')
        starexisted = Star.objects.filter(suname=username,stitle=startitle)
        if len(starexisted) == 0:
                Star.objects.create(suname=username,stitle=startitle)
                otherarticle = Article.objects.filter(aauthor=othername)
                otherlength = len(otherarticle)
                return render(request,'booklist/otherarticle.html',{'otherarticle':otherarticle,'otherlength':otherlength})
        else:
                othercontent=Article.objects.get(atitle=startitle)
                return render(request,'booklist/othercontent.html',{'othercontent':othercontent,'errors':'您已收藏过该笔记'})


             


#关注用户
def staruser(request):
        username=request.session.get('username')
        staruser = []
        staruser1 = StarUser.objects.filter(staruserauthor=username)
        for i in staruser1:
                tem = User.objects.get(uname = i.starusername)
                staruser.append(tem)
        starlength = len(staruser)
        return render(request,'booklist/staruser.html',{'staruser':staruser,'starlength':starlength})
def staruserarticle(request):
        otherarticle = Article.objects.filter(aauthor=request.GET['id'])
        request.session['aimusername']=request.GET['id']
        otherlength = len(otherarticle)
        return render(request,'booklist/staruserarticle.html',{'otherarticle':otherarticle,'otherlength':otherlength})
def starusercontent(request):
        starusercontent = Article.objects.get(atitle=request.GET['id'])
        return render(request,'booklist/starusercontent.html',{'starusercontent':starusercontent})
def searchuser(request):
        susername=request.session.get('susername')
        username=request.session.get('username')
        starexisted = StarUser.objects.filter(starusername=susername,staruserauthor=username)
        if len(starexisted) == 0:
                StarUser.objects.create(starusername=susername,staruserauthor=username)
                otheruser = User.objects.filter(uname=susername)
                return render(request,'booklist/otheruser.html',{'otheruser':otheruser})
        else:
                otheruser = User.objects.filter(uname=susername)
                return render(request,'booklist/otheruser.html',{'otheruser':otheruser,'errors':'您已关注过该用户'})



#上传笔记
def article(request):
        return render(request,'booklist/upload.html')
def getArticle(request):
        username=request.session.get('username')
        articleexisted=Article.objects.filter(atitle=request.GET['atitle'])
        if len(articleexisted)==0:
                Article.objects.create(atitle=request.GET['atitle'],abookname=request.GET['abookname'],awriter=request.GET['awriter'],acontent=request.GET['acontent'],aauthor=username)
                return render(request,'booklist/uploadsuccess.html')
        else:
                return render(request,'booklist/upload.html',{"errors":"该标题已存在,请您更换一个标题哦，亲"})
def change(request):
        content=request.GET['articletext']
        aimtitle=request.session.get('title')
        articlechanged=Article.objects.get(atitle=aimtitle)
        articlechanged.acontent=content
        articlechanged.save()
        username=request.session.get('username')
        personalarticle = Article.objects.filter(aauthor=username)  
        personallength=len(personalarticle) 
        return render(request,'booklist/personalarticle.html',{'personalarticle':personalarticle,'personallength':personallength})




#搜索指定书的笔记
def bookarticle(request):
        bookarticle = Article.objects.filter(abookname=request.GET["bbookname"])
        booklength=len(bookarticle)
        if booklength!=0:                                                 #如果这本书存在笔记
                request.session['bookname'] = bookarticle[0].abookname    #将搜索的书名存入session
        return render(request,'booklist/bookarticle.html',{'bookarticle':bookarticle,'booklength':booklength})    #存不存在笔记都运行这一行
def searchcontent(request):
        searchcontent = Article.objects.get(atitle=request.GET['id'])
        request.session['startitle']=searchcontent.atitle                 #将进入的笔记的名字存入session
        return render(request,'booklist/searchcontent.html',{'searchcontent':searchcontent})


#搜索用户
def otheruser(request):
        otherusername = request.GET["othername"]
        otheruser = User.objects.filter(uname=otherusername)
        if len(otheruser)==1:
                request.session['susername']=otheruser[0].uname
        return render(request,'booklist/otheruser.html',{'otheruser':otheruser,'otherusername':otherusername})
def otherarticle(request):
        otherperson = request.GET['id']
        otherarticle = Article.objects.filter(aauthor=otherperson)
        otherlength=len(otherarticle)
        if otherlength!= 0:
                request.session['othername'] = otherarticle[0].aauthor    #将搜索的用户名存入session
        return render(request,'booklist/otherarticle.html',{'otherarticle':otherarticle,'otherlength':otherlength,'otherperson':otherperson})
def othercontent(request):
        othercontent = Article.objects.get(atitle=request.GET['id'])
        request.session['startitle'] = othercontent.atitle
        return render(request,'booklist/othercontent.html',{'othercontent':othercontent})
def agreement(request):
        return render(request,'booklist/agreement.html')


    
