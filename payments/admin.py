from django.contrib import admin
from payments.models import Payment, Goods
# Register your models here.

class PaymentAdmin(admin.ModelAdmin):
	list_display = ('number','paymentDate', 'student', 'paymentType','item','price','note')

class GoodsAdmin(admin.ModelAdmin):
	list_display = ('code', 'item', 'price')
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Goods, GoodsAdmin)