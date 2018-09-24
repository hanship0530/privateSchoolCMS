from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Attendance
from students.models import Student
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import AttendanceForm

# Create your views here.
class AttendanceView(TemplateView):
	def searchStudent(request):
		if request.method == 'POST':
			html = {}
			try:
				name = request.POST['name']
				students = Student.objects.filter(stname=name)
				html['is_valid'] = True
				html['studentList'] = render_to_string('attendance/attendanceStudentList.html'
					,{'students':students},request=request)
				return JsonResponse(html)
			except Exception as e:
				print("Error"+str(e))
				html['is_valid'] = False
				html['errorMsg'] = "Error: "+str(e)
				return JsonResponse(html)
		else: # request.method == 'GET'
			return render(request, 'attendance/attendance.html', {})

	def getAttendList(request):
		if request.method == 'POST':
			html = {}
			try:
				number = request.POST['number']
				student = Student.objects.get(number=number)
				students = Student.objects.filter(stname=student.stname)
				attendData = student.attendance_set.all()
				attendList = []
				for row in attendData:
					temp = {}
					temp['number'] = str(row.number)
					temp['name'] = str(row.student.stname)
					temp['date'] = str(row.attendanceDate)
					temp['check'] = str(row.fillOut)
					attendList.append(temp)
				html['is_valid'] = True
				html['studentList'] = render_to_string('attendance/attendanceStudentList.html', {'students':students}, request=request)
				html['attendLists'] = render_to_string('attendance/attendanceTableList.html' ,{'attendList':attendList})
				return JsonResponse(html)
			except Exception as e:
				print("Error: "+str(e))
				html['is_valid'] = False
				html['errorMsg'] = "Error: "+str(e)
				return JsonResponse(html)
	def update(request, pk):
		attendance = get_object_or_404(Attendance, pk=pk)
		if request.method == 'POST':
			form = AttendanceForm(request.POST, instance=attendance)
		else:
			form = AttendanceForm(instance=attendance)
		return AttendanceView.saveAttendanceForm(request, form, 'attendance/attendancePartialUpdate.html', attendance)

	def saveAttendanceForm(request, form, template_name, attendance):
		html = {}
		try:
			if request.method == 'POST':
				if form.is_valid():
					form.save()
					html['form_is_valid'] = True
					students = Student.objects.filter(stname=attendance.student.stname)
					attendList = Attendance.objects.filter(student=attendance.student)
					html['studentList'] = render_to_string('attendance/attendanceStudentList.html', {'students':students})
					html['attendLists'] = render_to_string('attendance/attendanceTableList.html'
						,{'attendList':attendList})
				else:
					html['form_is_valid'] = False
					html['errorMsg'] = "form is not valid"
			context = {'form':form}
			html['html_form'] = render_to_string(template_name, context, request=request)
			return JsonResponse(html)
		
		except Exception as e:
			print("Error: "+str(e))
			html['form_is_valid'] = False
			html['errorMsg'] = "Error: "+str(e)
			return JsonResponse(html)