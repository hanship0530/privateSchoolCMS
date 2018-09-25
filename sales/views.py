from django.views.generic import TemplateView

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
import win32com.client, datetime, pythoncom, os, re, openpyxl
from django.utils import timezone
from payments.models import Payment
from .models import monthSale

# Create your views here.
class daySalesView(TemplateView):
	def display(request):
		try:
			html = {}
			if request.method == 'GET':
				wb = openpyxl.load_workbook('tutor_excel\\sales.xlsx')
				worksheets = wb.sheetnames
				html['sheets'] = render_to_string('sales/salesSheetSelect.html',{'worksheets':worksheets})
			return render(request,'sales/daySales.html',html)
		except Exception as e:
			print("Error: "+str(e))
			return redirect('dashboard:error')

	def makeDay(request):
		html = {}
		try:
			if request.method == 'GET':
				date = timezone.localtime(timezone.now()).date()
				payments = Payment.objects.filter(paymentDate=date, paymentState='결제')
				payment_refunds = Payment.objects.filter(paymentDate=date, paymentState='환불')
				total_Sales = 0
				total_payment = 0
				total_refunds = 0
				for sale in payments:
					total_payment = total_payment + sale.price
				for sale in payment_refunds:
					total_refunds = total_refunds + sale.price
				total_Sales = total_payment - total_refunds
				# Open Excel
				pythoncom.CoInitialize()
				excel = win32com.client.DispatchEx('Excel.Application')
				filepath = os.path.join(os.getcwd(), "tutor_excel\\sales.xlsx")
				workbook = excel.Workbooks.Open(filepath)
				excel.Visible = False
				excel.DisplayAlerts = False

				worksheet1 = workbook.Worksheets("main")
				worksheet2 = workbook.Worksheets.Add()
				sheetName = str(date)
				worksheet2.Name = sheetName
				worksheet2 = workbook.Worksheets(sheetName)
				worksheet1.Range("A1:AF100").Copy(worksheet2.Range("A1:AH41"))

				payment1 = ''
				payment2 = ''
				payment3 = ''
				payment4 = ''

				for payment in payments:
					if payment.paymentType == '카드':
						payment1 = payment1 + str(payment.student.stname)+'['+str(payment.student.stname)+']: '\
								   +str(payment.item)+'-'+str(payment.price)+'원, '
					else:
						payment2 = payment1 + str(payment.student.stname)+'['+str(payment.student.stname)+']: '\
								   +str(payment.item)+'-'+str(payment.price)+'원, '
				for payment in payment_refunds:
					if payment.paymentType == '카드':
						payment3 = payment1 + str(payment.student.stname)+'['+str(payment.student.stname)+']: '\
								   +str(payment.item)+'-'+str(payment.price)+'원, '
					else:
						payment4 = payment1 + str(payment.student.stname)+'['+str(payment.student.stname)+']: '\
								   +str(payment.item)+'-'+str(payment.price)+'원, '

				worksheet2.Range('B9').Value = payment1 # payment card
				worksheet2.Range('G9').Value = payment2 # payment casj
				worksheet2.Range('B28').Value = payment3 # refund card
				worksheet2.Range('G28').Value = payment4 # refund cash
				worksheet2.Range('C39').Value = total_Sales

				workbook.Save()
				workbook.Close(True)
				excel.Application.Quit()

				# Close Excel
				html['is_valid'] = True
				today = timezone.localtime(timezone.now()).date()
				month = monthSale(date=datetime(today.year, today.month), monthsales=total_Sales,
								  refundsCounts=payment_refunds.count(), paymentsCounts=payments.count())
			return JsonResponse(html)
		except Exception as e:
			print("Error: "+str(e))
			return redirect('dashboard:error')
