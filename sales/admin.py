from django.contrib import admin
from sales.models import Monthsale
# Register your models here.

class MonthsaleAdmin(admin.ModelAdmin):
	list_display = ('date','sales','refundsCounts','paymentsCounts')

admin.site.register(Monthsale, MonthsaleAdmin)
