from django import forms
from students.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('number','stname','prtname',
        	'address','contact','dateOfBirth','school','actState','isPayday','gender','lesson')

class StudentCreateForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ('number','stname','prtname',
        	'address','contact','dateOfBirth','school','actState','isPayday','gender','filepath','lesson')

class StudentSearchForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ('stname',)

class StudentLessonUpdateForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ('lesson',)
