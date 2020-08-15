from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Notice(models.Model):
	number = models.IntegerField(default=0, unique=True, verbose_name="작성번호", help_text='숫자만 입력하세요.')
	text = models.CharField(max_length=150, default='', verbose_name="내용", help_text='120자 이내로 입력하세요.')
	writer = models.CharField(max_length=20, default='', verbose_name='작성자', help_text='작성자를 입력하세요.')

	def __str__(self):
		return '['+self.writer+']의 공지사항'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fileName = models.FilePathField(path='tutor_excel/', verbose_name="강사시간표 파일명")

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()