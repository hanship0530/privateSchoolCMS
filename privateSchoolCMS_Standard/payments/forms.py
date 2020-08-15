from django import forms
from .models import Payment
from lessons.models import Lesson


class PaymentForm(forms.ModelForm):
    item = forms.ModelChoiceField(queryset=Lesson.objects.all(), empty_label="Please select.", label="수업/상품")
    class Meta:
        model = Payment
        fields = ('number', 'paymentDate','paymentType', 'paymentState', 'student', 'item', 'price', 'note')

class PaymentUpdateForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('number', 'paymentDate', 'paymentType', 'paymentState', 'student', 'item', 'price', 'note')