from django.db import models
from students.models import Student

# Create your models here.
class Attendance(models.Model):
	FILLOUT_CHOICE = (
		('작성','작성'),
		('미작성','미작성'),
	)
	number = models.AutoField(primary_key=True, verbose_name="번호")		
	attendanceDate = models.DateField(null=True, verbose_name="출석날짜")
	student = models.ForeignKey(Student, null=True)
	fillOut = models.CharField(max_length=6,null=True, default='미작성', choices=FILLOUT_CHOICE, verbose_name="차트작성여부")
	def __str__(self):
		return 'Student: '+self.student.stname+', Date: '+str(self.attendanceDate)