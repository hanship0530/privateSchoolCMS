from django import forms
from .models import Notice
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
	username = forms.CharField(max_length=10, required=True, help_text='영문 10자로 입력하세요.', label='아이디')
	password1 = forms.CharField(max_length=12, widget=forms.PasswordInput, label='비밀번호', help_text='최대 12자로 입력하세요.')
	password2 = forms.CharField(max_length=12, widget=forms.PasswordInput, label='비밀번호 확인', help_text='비밀번호 확인')
	first_name = forms.CharField(max_length=8, required=True, help_text='길동', label='이름')
	last_name = forms.CharField(max_length=4, required=True, help_text='홍', label='성')
	fileName = forms.FilePathField(path='tutor_excel/', label="강사시간표 파일명")
	class Meta:
		model = User
		fields = ('username', 'password1', 'password2', 'first_name', 'last_name','fileName')

class UpdateForm(UserCreationForm):
	password1 = forms.CharField(max_length=12, widget=forms.PasswordInput, label='이전 비밀번호', help_text='최대 12자로 입력하세요.')
	password2 = forms.CharField(max_length=12, widget=forms.PasswordInput, label='이전 비밀번호 확인', help_text='비밀번호 확인')
	new_password = forms.CharField(max_length=12, widget=forms.PasswordInput, label='새로운 비밀번호', help_text='최대 12자로 입력하세요.')
	first_name = forms.CharField(max_length=8, required=True, help_text='길동', label='이름')
	last_name = forms.CharField(max_length=4, required=True, help_text='홍', label='성')
	fileName = forms.FilePathField(path='tutor_excel/', label="강사시간표 파일명")
	class Meta:
		model = User
		fields = ('password1', 'password2', 'new_password', 'first_name', 'last_name','fileName')
class NoticeForm(forms.ModelForm):
	class Meta:
		model = Notice
		fields = ('number', 'text', 'writer')