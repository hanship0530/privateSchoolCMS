from django import forms
from .models import Payment, Goods
from .fields import SubjectModelChoiceField, PriceModelChoiceField


class PaymentForm(forms.ModelForm):
    item = forms.ModelChoiceField(queryset=Goods.objects.all(), empty_label="Please select.")
    class Meta:
        model = Payment
        fields = ('number', 'paymentDate','paymentType', 'student', 'item', 'note')



class GoodsForm(forms.ModelForm):
 	class Meta:
 		model = Goods
 		fields = ('code', 'item', 'price',)
