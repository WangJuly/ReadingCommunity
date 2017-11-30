"""dushubiji URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from booklist import views as booklist_views
urlpatterns = [
    #url(r'^$',booklist_views.index),
    url(r'index$',booklist_views.index,name='index'),
    url(r'getUser$',booklist_views.getUser,name='getUser'),
    url(r'first$',booklist_views.first,name='first'),
    url(r'login$',booklist_views.login,name='login'),
    url(r'getArticle$',booklist_views.getArticle,name='getArticle'),  
    url(r'Article$',booklist_views.article,name='Article'),
    url(r'Personal$',booklist_views.personal,name='Personal'),
    url(r'Personalarticle$',booklist_views.personalarticle,name='Personalarticle'),
    url(r'Personalcontent$',booklist_views.personalcontent,name='Personalcontent'),
    url(r'Stararticle$',booklist_views.stararticle,name='Stararticle'),
    url(r'Starcontent$',booklist_views.starcontent,name='Starcontent'),
    url(r'Bookarticle$',booklist_views.bookarticle,name='Bookarticle'),
    url(r'Searchcontent$',booklist_views.searchcontent,name='Searchcontent'),
    url(r'Delarticle$',booklist_views.delarticle,name='Delarticle'),
    url(r'Delstar$',booklist_views.delstar,name='Delstar'),
    url(r'Delstaruser$',booklist_views.delstaruser,name='Delstaruser'),
	url(r'Otheruser$',booklist_views.otheruser,name='Otheruser'),
	url(r'Otherarticle$',booklist_views.otherarticle,name='Otherarticle'),
	url(r'Othercontent$',booklist_views.othercontent,name='Othercontent'),
    url(r'Searchstar$',booklist_views.searchstar,name='Searchstar'),
	url(r'Searchuser$',booklist_views.searchuser,name='Searchuser'),
    url(r'Otherstar$',booklist_views.otherstar,name='Otherstar'),
    url(r'Change$',booklist_views.change,name='Change'),
    url(r'Agreement$',booklist_views.agreement,name='Agreement'),
	url(r'Staruser$',booklist_views.staruser,name='Staruser'),
	url(r'Staruserarticle$',booklist_views.staruserarticle,name='Staruserarticle'),
	url(r'Starusercontent$',booklist_views.starusercontent,name='Starusercontent'),
    url(r'^admin/', admin.site.urls),
]+staticfiles_urlpatterns()
