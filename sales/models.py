from django.db import models

# Create your models here.
class monthSale(models.Model):
	date = models.DateField(null=True, verbose_name="월")
	monthSale = models.IntegerField(null=True, verbose_name="월 매출")
	refundsCounts = models.IntegerField(null=True, verbose_name="월 매출")
	paymentsCounts = models.IntegerField(null=True, verbose_name="월 매출")
	def __str__(self):
		return str(date)+'['+str(monthsales)+']'
