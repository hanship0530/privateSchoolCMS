from django.db import models

# Create your models here.
class Note(models.Model):
	number = models.AutoField(primary_key=True, verbose_name="번호")	
	text = models.TextField(default=' ', verbose_name="내용")
	#writer = CharField()
