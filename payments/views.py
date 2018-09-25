from django.views.generic import TemplateView

from django.shortcuts import render
from .models import Goods, Payment
from .forms import GoodsForm, PaymentForm, PaymentUpdateForm
from django.template.loader import render_to_string
from students.models import Student
from students.forms import StudentSearchForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
# Create your views here.
class LessonManageView(TemplateView):
	def show(request):
		lessons = Goods.objects.all()
		return render(request, 'manageGoods/manageLesson.html', {'lessons':lessons})

	def saveLessonForm(template_name, form, request):
		html = {}
		if request.method == 'POST':
			if form.is_valid():
				form.save()
				html['form_is_valid'] = True
				lessons = Goods.objects.all()
				html['lesson_list'] = render_to_string('manageGoods/manageLessonPartialList.html', {'lessons':lessons})
			else:
				html['form_is_valid'] = False
		context = {'form':form}
		html['html_form'] = render_to_string(template_name, context, request=request)
		return JsonResponse(html)

	def create(request):
		if request.method == 'POST':
			form = GoodsForm(request.POST)
		else:
			form = GoodsForm()
		return LessonManageView.saveLessonForm('manageGoods/manageLessonPartialCreate.html', form, request)

	def update(request, pk):
		lesson = get_object_or_404(Goods, pk=pk)
		if request.method == 'POST':
			form = GoodsForm(request.POST, instance=lesson)
		else:
			form = GoodsForm(instance=lesson)
		return LessonManageView.saveLessonForm('manageGoods/manageLessonPartialUpdate.html', form, request)

	def delete(request, pk):
		lesson = get_object_or_404(Goods, pk=pk)
		html = {}
		if request.method == 'POST':
			lesson.delete()
			html['form_is_valid'] = True
			lessons = Goods.objects.all()
			html['lesson_list'] = render_to_string('manageGoods/manageLessonPartialList.html', {'lessons':lessons}
				, request=request)
		else:
			context = {'lesson':lesson}
			html['html_form'] = render_to_string('manageGoods/manageLessonPartialDelete.html', context, request=request)

		return JsonResponse(html)

class LessonCreateView(TemplateView):
    def create(request):
        if request.method == 'POST':
            form = GoodsForm(request.POST)
            return LessonCreateView.saveGoodsForm(request, form, 'manageGoods/manageLessonPartialCreate.html')  
        else:
            form = GoodsForm() 
            return render(request, 'manageGoods/manageLessonCreate.html', {'form':form})
    def saveGoodsForm(request, form, template_name):
        html = {}
        if request.method == 'POST':
            if form.is_valid():
                html['form_is_valid'] = True
                form.save()
                form = GoodsForm()
            else:
                html['form_is_valid'] = False   
        context = {'form':form}
        html['form_html'] = render_to_string(template_name, context, request=request)        
        return JsonResponse(html)    	

class PaymentManageView(TemplateView):
	def show(request):
		return render(request, 'payments/managePayment.html', {})

	def search(request):
		if request.method == 'POST':
			html = {}
			student = Student.objects.filter(stname=request.POST['name'])
			html['form_is_valid'] = True
			html['student_list'] = render_to_string('payments/managePaymentStudentList.html', {'students':student},
				request=request)
			html['payment_list'] = render_to_string('payments/managePaymentPartialList.html', {},
				request=request)			
		else:
			html['form_is_valid'] = False
			html['student_list'] = render_to_string('payments/managePaymentStudentList.html', {}, request=request)
			html['payment_list'] = render_to_string('payments/managePaymentPartialList.html', {},
				request=request)			
		return JsonResponse(html)

	def savePaymentForm(template_name, form, request, isNew):
		html = {}
		if request.method == 'POST':
			if form.is_valid():
				payment = form.save(commit=False)
				goods = Goods.objects.get(item=str(form.cleaned_data['item']).split('[')[0])
				payment.item = goods.item
				if form.cleaned_data['price'] == 0:
					payment.price = goods.price
				else:
					payment.price = form.cleaned_data['price']
				payment.student = form.cleaned_data['student']
				payment.save()
				student = payment.student
				if isNew:
					student.payment_set.add(payment)
				else:
					student.payment_set.update()
				html['form_is_valid'] = True
				students = Student.objects.filter(stname=student.stname)
				payments = student.payment_set.all()
				html['student_list'] = render_to_string('payments/managePaymentStudentList.html',{'students':students})
				html['payment_list'] = render_to_string('payments/managePaymentPartialList.html',{'payments':payments})
			else:
				html['form_is_valid'] = False
		context = {'form':form}
		html['html_form'] = render_to_string(template_name, context,request=request)
		return JsonResponse(html)

	def inquire(request, pk):
		student = get_object_or_404(Student, pk=pk)
		html = {}
		if request.method == 'GET':
			payments = student.payment_set.all()
			students = Student.objects.filter(stname=student.stname)
			html['form_is_valid'] = True
			html['student_list'] = render_to_string('payments/managePaymentStudentList.html', {'students':students},
				request=request)
			html['payment_list'] = render_to_string('payments/managePaymentPartialList.html', {'payments':payments},
				request=request)
		else:
			html['form_is_valid'] = False
			students = Student.objects.filter(stname=student.stname)
			html['student_list'] = render_to_string('payments/managePaymentStudentList.html', {'students':students},
				request=request)
			html['payment_list'] = render_to_string('payments/managePaymentPartialList.html', {},
				request=request)
		return JsonResponse(html)

	def create(request, pk):
		student = get_object_or_404(Student, pk=pk)
		if request.method == 'GET':
			form = PaymentForm(initial={'student': student})
		# get url can't move student obj to payments obj so should put sutdent to payments	
		return PaymentManageView.savePaymentForm('payments/managePaymentPartialCreate.html', form, request, True)		
	
	def createForm(request):
		if request.method == 'POST':
			form = PaymentForm(request.POST)
		return PaymentManageView.savePaymentForm('payments/managePaymentPartialCreate.html', form, request, True)

	def update(request, pk):
		payment = get_object_or_404(Payment, pk=pk)
		if request.method == 'POST':
			form = PaymentUpdateForm(request.POST, instance=payment)
		else:
			form = PaymentUpdateForm(instance=payment)
		return PaymentManageView.savePaymentForm('payments/managePaymentPartialUpdate.html', form, request, False)

	def delete(request, pk):
		payment = get_object_or_404(Payment, pk=pk)
		html = {}
		if request.method == 'POST':
			student = payment.student
			student.payment_set.remove(payment)
			payment.delete()
			html['form_is_valid'] = True
			payments = student.payment_set.all()
			students = Student.objects.filter(stname=student.stname)
			html['student_list'] = render_to_string('payments/managePaymentStudentList.html', {'students':students},
				request=request)
			html['payment_list'] = render_to_string('payments/managePaymentPartialList.html', {'payments':payments},
				request=request)
		else:
			context = {'payment':payment}
			html['html_form'] = render_to_string('payments/managePaymentPartialDelete.html', context, request=request)
		return JsonResponse(html)







