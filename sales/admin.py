from django.contrib import admin
from sales.models import monthSale
# Register your models here.

class monthSaleAdmin(admin.ModelAdmin):
	list_display = ('date','monthSale','refundsCounts','paymentsCounts')

admin.site.register(monthSale, monthSaleAdmin)
