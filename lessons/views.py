from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Lesson
from .forms import LessonForm
from django.template.loader import render_to_string
from students.models import Student
from students.forms import StudentSearchForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
# Create your views here.
class LessonManageView(TemplateView):
	def show(request):
		lessons = Lesson.objects.all()
		for lesson in lessons:
			number = lesson.student_set.all().count()
			lesson.people = number
			lesson.save()
		return render(request, 'manageGoods/manageLesson.html', {'lessons':lessons,'students':''})

	def saveLessonForm(template_name, form, request):
		html = {}
		if request.method == 'POST':
			if form.is_valid():
				form.save()
				html['form_is_valid'] = True
				lessons = Lesson.objects.all()
				html['lesson_list'] = render_to_string('manageGoods/manageLessonPartialList.html', {'lessons':lessons})
			else:
				html['form_is_valid'] = False
		context = {'form':form}
		html['html_form'] = render_to_string(template_name, context, request=request)
		return JsonResponse(html)

	def create(request):
		if request.method == 'POST':
			form = LessonForm(request.POST)
		else:
			form = LessonForm()
		return LessonManageView.saveLessonForm('manageGoods/manageLessonPartialCreate.html', form, request)

	def update(request, pk):
		lesson = get_object_or_404(Lesson, pk=pk)
		if request.method == 'POST':
			form = LessonForm(request.POST, instance=lesson)
		else:
			form = LessonForm(instance=lesson)
		return LessonManageView.saveLessonForm('manageGoods/manageLessonPartialUpdate.html', form, request)

	def delete(request, pk):
		lesson = get_object_or_404(Lesson, pk=pk)
		html = {}
		if request.method == 'POST':
			lesson.delete()
			html['form_is_valid'] = True
			lessons = Lesson.objects.all()
			html['lesson_list'] = render_to_string('manageGoods/manageLessonPartialList.html', {'lessons':lessons}
				, request=request)
		else:
			context = {'lesson':lesson}
			html['html_form'] = render_to_string('manageGoods/manageLessonPartialDelete.html', context, request=request)

		return JsonResponse(html)
	
	def inquire(request, pk):
		lesson = get_object_or_404(Lesson, pk=pk)
		html = {}
		try:
			if request.method == 'GET':
				lessons = Lesson.objects.all()
				students = lesson.student_set.all()
				html['studentList'] = render_to_string('manageGoods/manageLessonStudentPartialList.html',
					{'students':students}, request=request)
				return JsonResponse(html)
		except Exception as e:
			print("Error: "+str(e))
			return redirect('dashboard:error')
			
	def deleteStudentLesson(request, pk):
		try:
			html = {}
			if request.method == 'GET':
				student = get_object_or_404(Student, pk=pk)
				lesson = Lesson.objects.get(student=student)
				student.lesson = None
				student.save()
				lessons = Lesson.objects.all()
				students = lesson.student_set.all()	
				print(student)			
				html['studentList'] = render_to_string('manageGoods/manageLessonStudentPartialList.html',
					{'students':students}, request=request)
				return JsonResponse(html)
		except Exception as e:
			print("Error: "+str(e))
			return redirect('dashboard:error')

class LessonCreateView(TemplateView):
    def create(request):
        if request.method == 'POST':
            form = LessonForm(request.POST)
            return LessonCreateView.saveLessonForm(request, form, 'manageGoods/manageLessonPartialCreate.html')  
        else:
            form = LessonForm() 
            return render(request, 'manageGoods/manageLessonCreate.html', {'form':form})
    def saveLessonForm(request, form, template_name):
        html = {}
        if request.method == 'POST':
            if form.is_valid():
                html['form_is_valid'] = True
                form.save()
                form = LessonForm()
            else:
                html['form_is_valid'] = False   
        context = {'form':form}
        html['form_html'] = render_to_string(template_name, context, request=request)        
        return JsonResponse(html)   