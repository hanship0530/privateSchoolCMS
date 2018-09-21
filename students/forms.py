from django import forms
from students.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('number','stname','prtname',
        	'address','contact','dateOfBirth','school','actState','isPayday','gender',)

class StudentCreateForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ('number','stname','prtname',
        	'address','contact','dateOfBirth','school','actState','isPayday','gender','filepath',)

class StudentSearchForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ('stname',)