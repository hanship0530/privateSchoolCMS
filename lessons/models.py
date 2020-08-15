from django.db import models

# Create your models here.
class Lesson(models.Model):
	code = models.AutoField(primary_key=True, verbose_name="Merchant Code")
	item = models.CharField(max_length=10, unique=True, default='', verbose_name="수업", help_text="최대 20자까지 입력가능")
	price = models.IntegerField(default=0, verbose_name="가격", help_text="숫자만 입력하세요.")
	teacher = models.CharField(max_length=10, null=True, default='', verbose_name="강사", help_text="강사명")
	days = models.CharField(max_length=10, null=True, default='', verbose_name="수업요일", help_text="예시: 월/목")
	people = models.IntegerField(default=0, blank=True, null=True, verbose_name="수강생 수")
	def __str__(self):
		return str(self.item)+'['+str(self.price)+']원'