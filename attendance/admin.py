from django.contrib import admin
from attendance.models import Attendance 

# Register your models here.
class AttendanceAdmin(admin.ModelAdmin):
	list_display = ('attendanceDate', 'student', 'fillOut')

admin.site.register(Attendance, AttendanceAdmin)
