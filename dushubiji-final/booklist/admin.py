from django.contrib import admin
from .models import *
#Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	list_display=('atitle','aauthor','abookname')
class UserAdmin(admin.ModelAdmin):
	list_display=('uname','uage')
class StarAdmin(admin.ModelAdmin):
	list_display=('suname','stitle')
class StarUserAdmin(admin.ModelAdmin):
	list_display=('starusername','staruserauthor')
admin.site.register(Star,StarAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(StarUser,StarUserAdmin)