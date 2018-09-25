from django import forms
from .models import Payment, Goods


class PaymentForm(forms.ModelForm):
    item = forms.ModelChoiceField(queryset=Goods.objects.all(), empty_label="Please select.", label="수업/상품")
    class Meta:
        model = Payment
        fields = ('number', 'paymentDate','paymentType', 'paymentState', 'student', 'item', 'price', 'note')

class PaymentUpdateForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('number', 'paymentDate', 'paymentType', 'paymentState', 'student', 'item', 'price', 'note')

class GoodsForm(forms.ModelForm):
 	class Meta:
 		model = Goods
 		fields = ('code', 'item', 'price',)
