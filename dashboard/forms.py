from django import forms
from .models import Notice
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=True, help_text='Optional.', label='이름')
	last_name = forms.CharField(max_length=30, required=True, help_text='Optional.', label='성')
	fileName = forms.FilePathField(path='tutor_excel/', label="강사시간표 파일명")
	class Meta:
		model = User
		fields = ('username', 'password1', 'password2', 'first_name', 'last_name','fileName')

class NoticeForm(forms.ModelForm):
	class Meta:
		model = Notice
		fields = ('number', 'text', 'writer')