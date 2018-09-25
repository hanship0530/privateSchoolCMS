from django.contrib import admin
from lessons.models import Lesson
# Register your models here.
class LessonAdmin(admin.ModelAdmin):
	list_display = ('code', 'item', 'price','teacher','days')
	
admin.site.register(Lesson, LessonAdmin)