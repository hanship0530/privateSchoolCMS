from django.views.generic import TemplateView

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
import win32com.client, datetime, pythoncom, os, re, openpyxl
from django.utils import timezone
from payments.models import Payment
from .models import Monthsale

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
				wb = openpyxl.load_workbook("tutor_excel\\sales.xlsx")
				worksheets = wb.sheetnames
				date = timezone.localtime(timezone.now()).date()
				if str(date) not in worksheets:
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
							payment1=payment1+str(payment.student.stname)+"["+str(payment.student.number)+"]: "+str(payment.item)+"-"+str(payment.price)+"원,\n"
						else:
							payment2=payment2+str(payment.student.stname)+'['+str(payment.student.number)+']: '+str(payment.item)+'-'+str(payment.price)+'원,\n'
					for payment in payment_refunds:
						if payment.paymentType == '카드':
							payment3 = payment3+str(payment.student.stname)+'['+str(payment.student.number)+']: '+str(payment.item)+'-'+str(payment.price)+'원,\n'
						else:
							payment4=payment4+str(payment.student.stname)+'['+str(payment.student.number)+']: '+str(payment.item)+'-'+str(payment.price)+'원,\n'

					worksheet2.Range('B9').Value = payment1 # payment card
					worksheet2.Range('B9').Font.Size = 9
					worksheet2.Range('G9').Value = payment2 # payment casj
					worksheet2.Range('G9').Font.Size = 9
					worksheet2.Range('B28').Value = payment3 # refund card
					worksheet2.Range('B28').Font.Size = 9
					worksheet2.Range('G28').Value = payment4 # refund cash
					worksheet2.Range('G28').Font.Size = 9
					worksheet2.Range('C39').Value = total_Sales

					workbook.Save()
					workbook.Close(True)
					excel.Application.Quit()
					# Close Excel

					html['is_valid'] = True
					wb = openpyxl.load_workbook("tutor_excel\\sales.xlsx")
					worksheets = wb.sheetnames
					html['sheets'] = render_to_string('sales/salesSheetSelect.html',{'worksheets':worksheets})

					today = timezone.localtime(timezone.now()).date()
					# print(today.strftime("%y-%m"))
					if Monthsale.objects.filter(date=datetime.datetime(today.year, today.month, 1)).exists():
						month = Monthsale.objects.get(date=datetime.datetime(today.year, today.month, 1))
						month.sales = month.sales + total_Sales
						month.refundsCounts = month.refundsCounts + payment_refunds.count()
						month.paymentsCounts = month.paymentsCounts + payments.count()
						month.save()
					else:
						month = Monthsale(date=datetime.datetime(today.year, today.month, 1), sales=total_Sales, 
							refundsCounts=payment_refunds.count(), paymentsCounts=payments.count())
						month.save()
				else:
					html['is_valid'] = False
					html['sheets'] = render_to_string('sales/salesSheetSelect.html',{'worksheets':worksheets})
					html['errorMsg'] = '이미 작성했습니다. 엑셀 시트를 확인해주세요.'
			return JsonResponse(html)
		except Exception as e:
			print("Error: "+str(e))
			return redirect('dashboard:error')

	def inquire(request):
		html = {}
		try:
			if request.method == 'POST':
				sheet = request.POST['sheet']
				wb = openpyxl.load_workbook("tutor_excel\\sales.xlsx")
				ws = wb[sheet]
				html['is_valid'] = True
				paymentCard = str(ws['B9'].value).replace("\n","").split(',')
				paymentCash = str(ws['G9'].value).replace("\n","").split(',')
				refundCard = str(ws['B28'].value).replace("\n","").split(',')
				refundCash = str(ws['G28'].value).replace("\n","").split(',')
				html['paymentCard'] = render_to_string('sales/daySales_paymentCard.html',{'paymentCard':paymentCard})
				html['paymentCash'] = render_to_string('sales/daySales_paymentCash.html',{'paymentCash':paymentCash})
				html['refundCard'] = render_to_string('sales/daySales_refundCard.html',{'refundCard':refundCard})
				html['refundCash'] = render_to_string('sales/daySales_refundCash.html',{'refundCash':refundCash})
				html['total'] = str(format(int(ws['C39'].value),','))+'원'
				worksheets = wb.sheetnames
				html['sheets'] = render_to_string('sales/salesSheetSelect.html',{'worksheets':worksheets})
				return JsonResponse(html)
		except Exception as e:
			print("Error: "+str(e))
			return redirect('dashboard:error')

class motnthSaleView(TemplateView):
	template_name = "sales/monthSales.html"
	def get_context_data(self, **kwargs):
		context = super(motnthSaleView, self).get_context_data(**kwargs)
		monthsales = Monthsale.objects.all()
		topsevens = monthsales[:7]
		monthsalesHtml = render_to_string('sales/monthSalesList.html',{'monthsales':monthsales})
		context.update({'topsevens': topsevens, 'monthsalesHtml':monthsalesHtml})
		return context