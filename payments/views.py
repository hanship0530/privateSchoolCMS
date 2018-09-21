from django.views.generic import TemplateView

from django.shortcuts import render
from .models import Goods, Payment
from .forms import GoodsForm, PaymentForm
from django.template.loader import render_to_string
from students.models import Student
from students.forms import StudentSearchForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse


# Create your views here.
class LessonManageView(TemplateView):
	def show(request):
		lessons = Goods.objects.all()
		return render(request, 'components/manageLesson.html', {'lessons':lessons})

	def saveLessonForm(template_name, form, request):
		ht_data = dict()
		if request.method == 'POST':
			if form.is_valid():
				form.save()
				ht_data['form_is_valid'] = True
				lessons = Goods.objects.all()
				ht_data['lesson_list'] = render_to_string('components/manageLessonPartialList.html', {'lessons':lessons})
			else:
				ht_data['form_is_valid'] = False
		context = {'form':form}
		ht_data['html_form'] = render_to_string(template_name, context, request=request)
		return JsonResponse(ht_data)

	def create(request):
		if request.method == 'POST':
			form = GoodsForm(request.POST)
		else:
			form = GoodsForm()
		return LessonManageView.saveLessonForm('components/manageLessonPartialCreate.html', form, request)

	def update(request, pk):
		lesson = get_object_or_404(Goods, pk=pk)
		if request.method == 'POST':
			form = GoodsForm(request.POST, instance=lesson)
		else:
			form = GoodsForm(instance=lesson)
		return LessonManageView.saveLessonForm('components/manageLessonPartialUpdate.html', form, request)

	def delete(request, pk):
		lesson = get_object_or_404(Goods, pk=pk)
		ht_data = dict()
		if request.method == 'POST':
			lesson.delete()
			ht_data['form_is_valid'] = True
			lessons = Goods.objects.all()
			ht_data['lesson_list'] = render_to_string('components/manageLessonPartialList.html', {'lessons':lessons}
				, request=request)
		else:
			context = {'lesson':lesson}
			ht_data['html_form'] = render_to_string('components/manageLessonPartialDelete.html', context, request=request)

		return JsonResponse(ht_data)

class PaymentManageView(TemplateView):
	def show(request):
		return render(request, 'components/managePayment.html', {})

	def search(request):
		if request.method == 'POST':
			ht_data = {}
			student = Student.objects.filter(stname=request.POST['name'])
			ht_data['form_is_valid'] = True
			ht_data['student_list'] = render_to_string('components/managePaymentStudentList.html', {'students':student},
				request=request)
			ht_data['payment_list'] = render_to_string('components/managePaymentPartialList.html', {},
				request=request)			
		else:
			ht_data['form_is_valid'] = False
			ht_data['student_list'] = render_to_string('components/managePaymentStudentList.html', {}, request=request)
			ht_data['payment_list'] = render_to_string('components/managePaymentPartialList.html', {},
				request=request)			
		return JsonResponse(ht_data)

	def savePaymentForm(template_name, form, request, isNew):
		ht_data = dict()
		if request.method == 'POST':
			if form.is_valid():
				payment = form.save(commit=False)
				payment.item = form.cleaned_data['item'].item
				payment.price = form.cleaned_data['item'].price
				payment.student = form.cleaned_data['student']
				payment.save()
				student = payment.student
				if isNew:
					student.payment_set.add(payment)
				else:
					student.payment_set.update()
				ht_data['form_is_valid'] = True
				students = Student.objects.filter(stname=student.stname)
				payments = student.payment_set.all()
				ht_data['student_list'] = render_to_string('components/managePaymentStudentList.html',{'students':students})
				ht_data['payment_list'] = render_to_string('components/managePaymentPartialList.html',{'payments':payments})
			else:
				ht_data['form_is_valid'] = False
		context = {'form':form}
		ht_data['html_form'] = render_to_string(template_name, context, request=request)
		return JsonResponse(ht_data)

	def inquire(request, pk):
		student = get_object_or_404(Student, pk=pk)
		ht_data = {}
		if request.method == 'GET':
			payments = student.payment_set.all()
			students = Student.objects.filter(stname=student.stname)
			ht_data['form_is_valid'] = True
			ht_data['student_list'] = render_to_string('components/managePaymentStudentList.html', {'students':students},
				request=request)
			ht_data['payment_list'] = render_to_string('components/managePaymentPartialList.html', {'payments':payments},
				request=request)
		else:
			ht_data['form_is_valid'] = False
			students = Student.objects.filter(stname=student.stname)
			ht_data['student_list'] = render_to_string('components/managePaymentStudentList.html', {'students':students},
				request=request)
			ht_data['payment_list'] = render_to_string('components/managePaymentPartialList.html', {},
				request=request)
		return JsonResponse(ht_data)

	def create(request, pk):
		student = get_object_or_404(Student, pk=pk)
		if request.method == 'GET':
			form = PaymentForm(initial={'student': student})
		# get url can't move student obj to payments obj so should put sutdent to payments	
		return PaymentManageView.savePaymentForm('components/managePaymentPartialCreate.html', form, request, True)		
	
	def createForm(request):
		if request.method == 'POST':
			form = PaymentForm(request.POST)
		return PaymentManageView.savePaymentForm('components/managePaymentPartialCreate.html', form, request, True)
	
	def update(request, pk):
		payment = get_object_or_404(Payment, pk=pk)
		if request.method == 'POST':
			form = PaymentForm(request.POST, instance=payment)
		else:
			form = PaymentForm(instance=payment)
		return PaymentManageView.savePaymentForm('components/managePaymentPartialUpdate.html', form, request, False)

	def delete(request, pk):
		payment = get_object_or_404(Payment, pk=pk)
		ht_data = dict()
		if request.method == 'POST':
			student = payment.student
			student.payment_set.remove(payment)
			payment.delete()
			ht_data['form_is_valid'] = True
			payments = student.payment_set.all()
			students = Student.objects.filter(stname=student.stname)
			ht_data['student_list'] = render_to_string('components/managePaymentStudentList.html', {'students':students},
				request=request)
			ht_data['payment_list'] = render_to_string('components/managePaymentPartialList.html', {'payments':payments},
				request=request)
		else:
			context = {'payment':payment}
			ht_data['html_form'] = render_to_string('components/managePaymentPartialDelete.html', context, request=request)
		return JsonResponse(ht_data)







