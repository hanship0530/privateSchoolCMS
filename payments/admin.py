from django.contrib import admin
from payments.models import Payment
# Register your models here.

class PaymentAdmin(admin.ModelAdmin):
	list_display = ('number','paymentDate', 'student', 'paymentType', 'paymentState', 'item', 'price', 'note')
	
admin.site.register(Payment, PaymentAdmin)