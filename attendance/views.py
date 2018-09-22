from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Attendance
from students.models import Student
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

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
					temp['date'] = str(row.attendanceDate)
					temp['check'] = str(row.fillOut)
					attendList.append(temp)
				html['is_valid'] = True
				html['studentList'] = render_to_string('attendance/attendanceStudentList.html', {'students':students}, request=request)
				html['attendLists'] = render_to_string('attendance/attendanceTableList.html'
					,{'attendList':attendList})
				return JsonResponse(html)
			except Exception as e:
				print("Error: "+str(e))
				html['is_valid'] = False
				html['errorMsg'] = "Error: "+str(e)
				return JsonResponse(html)
				

