from django.db import models
import os, datetime
from django.utils import timezone
from shutil import copyfile

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
	stname = models.CharField(max_length=10, blank=False, null=True, verbose_name="회원이름", help_text='홍길동')
	prtname = models.CharField(max_length=10, blank=False, null=True, verbose_name="보호자 성함", help_text='홍길동')
	contact = models.CharField(max_length=11, blank=False, null=True, verbose_name="보호자 연락처", help_text='010-0000-0000')
	address = models.CharField(max_length=100, blank=False, null=True, verbose_name="주소", help_text='서울시 서울대로 25')
	dateOfBirth = models.DateField(blank=False, null=False, verbose_name="생년월일", help_text='2000-01-01')
	dateOfEnroll = models.DateField(default=timezone.now, blank=True, null=True, verbose_name="가입일")
	actState = models.CharField(max_length=6, null=True, default='ACTIVE',choices=SATUS_CHOICE, verbose_name="회원상태")
	isPayday = models.CharField(max_length=10, blank=False, null=True, default='PAYED', choices=PAYMEMENT_CHOICE, verbose_name="결제일 여부")
	exceedCount = models.IntegerField(default=0, blank=True, null=True, verbose_name="초과횟수", help_text='수업을 초과한 횟수를 입력하세요.')
	classCount = models.IntegerField(default=0, blank=True, null=True, verbose_name="남는 수업횟수") 
	gender = models.CharField(max_length=2, null=True, choices=GENDER_CHOICE, verbose_name="성별")
	school = models.CharField(max_length=20, blank=False, null=True, verbose_name="학교")
	years = models.CharField(max_length=4, blank=True, null=True, verbose_name="학년")
	sheet = models.CharField(max_length=10, blank=True, null=True, default="main", verbose_name="현재시트명")
	filepath = models.CharField(max_length=50, blank=True, null=True, verbose_name="차트파일 위치")

	def __str__(self):
		return str(self.stname)+'['+str(self.number)+']'

	def save(self, *args, **kwargs):
		if(not os.path.isfile(os.path.join(os.getcwd(),"student_excel\\"+str(self.number)+"_"+str(self.stname)+"_차트.xlsx"))):
			copyfile(os.path.join(os.getcwd(),"student_excel\\studentchart.xlsx"), 
				os.path.join(os.getcwd(),"student_excel\\"+str(self.number)+"_"+str(self.stname)+"_차트.xlsx"))
			self.filepath = "student_excel\\"+str(self.number)+"_"+str(self.stname)+"_차트.xlsx"
		super().save(*args, **kwargs)

