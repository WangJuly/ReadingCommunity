from django.contrib import admin
from .models import *
# Register your models here.
class BookAdmin(admin.ModelAdmin):
	list_display=('btitle','btutor')
class UserAdmin(admin.ModelAdmin):
	list_display=('uname','uage')
admin.site.register(Book,BookAdmin)
admin.site.register(User,UserAdmin)