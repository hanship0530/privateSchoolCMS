from django.db import models

# Create your models here.
class Monthsale(models.Model):
	date = models.DateField(null=True, verbose_name="월")
	sales = models.IntegerField(null=True, verbose_name="월 매출")
	refundsCounts = models.IntegerField(null=True, verbose_name="환불 횟수")
	paymentsCounts = models.IntegerField(null=True, verbose_name="결제 횟수")
	def __str__(self):
		return '['+str(self.date.strftime("%y-%m"))+'월 매출]: '+str(self.sales)+'원'
