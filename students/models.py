from django.db import models
import os, datetime
from django.utils import timezone
from django.utils.timezone import localtime, now
from shutil import copyfile
from lessons.models import Lesson

# Create your models here. 
class Student(models.Model):
	SATUS_CHOICE = (
		('HUMAN','휴먼'),
		('ACTIVE','활성화'),
	)
	PAYMEMENT_CHOICE = (
		('PAY','결제일'),
		('PAYED','비결제일'),
	)
	GENDER_CHOICE = (
		('M','남'),
		('F','여')
	)
	number = models.IntegerField(blank=False, null=True, unique=True, verbose_name="회원번호", help_text='0이상의 숫자를 입력해주세요.')
	stname = models.CharField(max_length=10, blank=False, null=True, verbose_name="회원이름", help_text='최대 10자까지 입력가능')
	prtname = models.CharField(max_length=10, blank=False, null=True, verbose_name="보호자 성함", help_text='최대 10자까지 입력가능')
	contact = models.CharField(max_length=11, blank=False, null=True, verbose_name="보호자 연락처", help_text='010-XXXX-XXXX')
	address = models.CharField(max_length=100, blank=False, null=True, verbose_name="주소", help_text='00시 000로 건물번호 세부주소')
	dateOfBirth = models.DateField(blank=False, null=False, verbose_name="생년월일", help_text='YYYY-MM-DD')
	dateOfEnroll = models.DateField(default=timezone.now, blank=True, null=True, verbose_name="가입일")
	actState = models.CharField(max_length=6, null=True, default='ACTIVE',choices=SATUS_CHOICE, verbose_name="회원상태")
	isPayday = models.CharField(max_length=10, blank=False, null=True, default='PAYED', choices=PAYMEMENT_CHOICE, verbose_name="결제일 여부")
	# exceedCount = models.IntegerField(default=0, blank=True, null=True, verbose_name="초과횟수", help_text='수업을 초과한 횟수를 입력하세요.')
	# classCount = models.IntegerField(default=0, blank=True, null=True, verbose_name="남는 수업횟수") 
	gender = models.CharField(max_length=2, null=True, choices=GENDER_CHOICE, verbose_name="성별")
	school = models.CharField(max_length=20, blank=False, null=True, verbose_name="학교", help_text="XXX중학교")
	years = models.CharField(max_length=4, blank=True, null=True, verbose_name="학년")
	sheet = models.CharField(max_length=10, blank=True, null=True, default="main", verbose_name="현재시트명")
	filepath = models.CharField(max_length=50, blank=True, null=True, verbose_name="차트파일 위치")
	lesson = models.ForeignKey(Lesson, null=True, verbose_name="수업", on_delete=models.CASCADE)
	def __str__(self):
		return str(self.stname)+'['+str(self.number)+']'

	def save(self, *args, **kwargs):
		year1 = str(localtime(now()).date()).split('-')[0]
		year2 = str(self.dateOfBirth).split('-')[0]
		year = int(year1) - int(year2)
		if year == 8:
			self.years = "초1"
		elif year == 9:
			self.years = "초2"
		elif year == 10:
			self.years = "초3"
		elif year == 11:
			self.years = "초4"
		elif year == 12:
			self.years = "초5"
		elif year == 13:
			self.years = "초6"
		elif year == 14:
			self.years = "중1"
		elif year == 15:
			self.years = "중2"
		elif year == 16:
			self.years = "중3"
		elif year == 17:
			self.years = "고1"
		elif year == 18:
			self.years = "고2"
		elif year == 19:
			self.years = "고3"	
		else:
			self.years = "유년/성년"
		if(not os.path.isfile(os.path.join(os.getcwd(),"student_excel\\"+str(self.number)+"_"+str(self.stname)+"_차트.xlsx"))):
			copyfile(os.path.join(os.getcwd(),"student_excel\\studentchart.xlsx"), 
				os.path.join(os.getcwd(),"student_excel\\"+str(self.number)+"_"+str(self.stname)+"_차트.xlsx"))
			self.filepath = "student_excel\\"+str(self.number)+"_"+str(self.stname)+"_차트.xlsx"
		super().save(*args, **kwargs)

