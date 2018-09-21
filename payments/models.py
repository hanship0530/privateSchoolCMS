from django.db import models
from students.models import Student
from django.utils import timezone

# Create your models here.
class Payment(models.Model):
	PAYMENT_CHOICE = (
		('CREDIT','카드'),
		('CASH','현금'),
	)
	number = models.AutoField(primary_key=True, verbose_name="번호")	
	paymentDate = models.DateField(default=timezone.now, verbose_name="결제일")
	student = models.ForeignKey(Student, null=True, verbose_name="학생", on_delete=models.CASCADE)
	paymentType = models.CharField(max_length=6, choices=PAYMENT_CHOICE, default='CREDIT', verbose_name="결제방식")
	item = models.CharField(max_length=30, null=True, verbose_name="상품")
	price = models.IntegerField(default=0, verbose_name="가격")
	note = models.CharField(max_length=100, default='', verbose_name="Memo")
	def __str__(self):
		return str(self.paymentDate)+"_"+str(self.student)

class Goods(models.Model):
	code = models.AutoField(primary_key=True, verbose_name="Merchant Code")
	item = models.CharField(max_length=10, default='', verbose_name="상품")
	price = models.IntegerField(default=0, verbose_name="가격")
	def __str__(self):
		return str(self.item)+"_"+str(self.price)