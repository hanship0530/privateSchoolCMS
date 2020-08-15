from django.db import models
from students.models import Student
from django.utils import timezone

# Create your models here.
class Payment(models.Model):
	PAYMENT_CHOICE = (
		('카드','카드'),
		('현금','현금'),
	)
	PAYMENT_STATE = (
		('결제','결제'),
		('환불','환불'),
	)
	number = models.AutoField(primary_key=True, verbose_name="번호")	
	paymentDate = models.DateField(default=timezone.now, verbose_name="결제일")
	student = models.ForeignKey(Student, null=True, verbose_name="학생", on_delete=models.CASCADE)
	paymentType = models.CharField(max_length=6, choices=PAYMENT_CHOICE, default='카드', verbose_name="결제방식")
	paymentState = models.CharField(max_length=6, choices=PAYMENT_STATE, default='결제', verbose_name="결제상태")
	item = models.CharField(max_length=30, null=True, verbose_name="수업/상품")
	price = models.IntegerField(default=0, blank=True, verbose_name="가격")
	note = models.CharField(max_length=100, blank=True, default='', null=True, verbose_name="Memo")
	def __str__(self):
		return str(self.student)+'의 결제['+str(self.paymentDate)+']'