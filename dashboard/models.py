from django.db import models

# Create your models here.
class Notice(models.Model):
	number = models.IntegerField(default=0, unique=True, verbose_name="작성번호", help_text='숫자만 입력하세요.')
	text = models.CharField(max_length=150, default='', verbose_name="내용", help_text='120자 이내로 입력하세요.')
	writer = models.CharField(max_length=20, default='', verbose_name='작성자', help_text='작성자를 입력하세요.')

	def __str__(self):
		return '['+self.writer+']의 공지사항'