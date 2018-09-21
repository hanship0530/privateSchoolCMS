from django.db import models
from students.models import Student

# Create your models here.
class Attendance(models.Model):
	attendanceDate = models.DateField(null=True, verbose_name="출석날짜")
	student = models.ForeignKey(Student, null=True)
	fillOut = models.BooleanField(default=False, verbose_name="차트작성여부")
	def __str__(self):
		return 'Student: '+self.student.stname+', Date: '+str(self.attendanceDate)