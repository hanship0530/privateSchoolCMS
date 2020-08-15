from django.contrib import admin
from .models import Notice

# Register your models here.
class NoticeAdmin(admin.ModelAdmin):
	list_display = ('number', 'text', 'writer')
admin.site.register(Notice, NoticeAdmin)
