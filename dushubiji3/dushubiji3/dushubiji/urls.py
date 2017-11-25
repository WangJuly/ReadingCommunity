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
from booklist import views as booklist_views
urlpatterns = [
    #url(r'^$',booklist_views.index),
    url(r'^$',booklist_views.index,name='index'),
    url(r'^getUser$',booklist_views.getUser,name='getUser'),
    url(r'^getArticle$',booklist_views.getArticle,name='getArticle'),  
    url(r'^Article$',booklist_views.article,name='Article'),
    url(r'Personal$',booklist_views.personal,name='Personal'),
    url(r'Personalarticle$',booklist_views.personalarticle,name='Personalarticle'),
	url(r'Bookarticle$',booklist_views.bookarticle,name='Bookarticle'),
	url(r'search$',booklist_views.search,name='search'),
    url(r'^admin/', admin.site.urls),
]
