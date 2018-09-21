from django.contrib import admin
from students.models import Student # student 모델에서 Student 클래스는 임포트
# Register your models here.
# 장고 어드민 사이트에 반영함

class StudentAdmin(admin.ModelAdmin):
	list_display = ('number','stname','prtname','address','contact','dateOfBirth',
		'dateOfEnroll','actState','isPayday','exceedCount','school','years','classCount','gender','sheet','filepath',)

admin.site.register(Student, StudentAdmin)	
