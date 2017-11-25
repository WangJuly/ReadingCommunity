from django.contrib import admin
from .models import *
#Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	list_display=('atitle','aauthor','abookname')
class UserAdmin(admin.ModelAdmin):
	list_display=('uname','uage','uarticlenumber')
class BookAdmin(admin.ModelAdmin):
    list_display=('bbookname','bwriter','barticlenumber')
admin.site.register(Article,ArticleAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Book,BookAdmin)
