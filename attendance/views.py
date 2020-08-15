from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Attendance
from students.models import Student
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import AttendanceForm
from django.utils import timezone
from .arduinoAttendanceFunction import getRfidCardNumber, stopReadRfidCard
import serial

# Create your views here.
class AttendanceView(TemplateView):
	def searchStudent(request):
		html = {}
		if request.method == 'POST':
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
		html = {}
		if request.method == 'POST':
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
	#new
	def registerCardNumber(request):
		html={}
		if request.method == 'POST':
			try:
				number = int(request.POST['number'])
				student = Student.objects.get(number=number)
				cardNumber = getRfidCardNumber()
				student.attendanceCardNumber = cardNumber
				student.save()
				html['isSuccess']=True
				html['successMessageAjax']=student.stname + "'s card is registered!"
				return JsonResponse(html)
			except Exception as e:
				print("Error: " + str(e))
				html['isSuccess']=False
				html['errorMessage']='Port is not exist'
				return redirect('dashboard:error')
	def stopTagStudentAttendance(request):
		if request.method == 'POST':
			print("stop")
			stopReadRfidCard()
			return redirect('dashboard:index')
	def tagStudentAttendance(request):
		if request.method == 'POST':
			html = {}
			try:
				cardNumber = getRfidCardNumber()
				student = Student.objects.get(attendanceCardNumber=cardNumber)
				today = timezone.localtime(timezone.now()).date()
				attendance = Attendance(attendanceDate=today, student=student)
				isAttend = student.attendance_set.filter(attendanceDate=today, student=student)
				if not isAttend:
					attendance.save()
					student.attendance_set.add(attendance)
				html['attendanceInformation'] = student.stname+' attend now!'
				return JsonResponse(html)
			except Exception as e:
				print("Error: " + str(e))
				html['attendanceInformation']='Already Attend Or Your card IS NOT registered'
				return JsonResponse(html)
		if request.method == 'GET':
			return render(request,'attendance/tagAttendanceCard.html',{
				'notice':"Click 'Attend Now' to attend Private School",
				'instruction': "Put your card on card reader after click 'Attend Now' Button"
				})
	def update(request, pk):
		attendance = get_object_or_404(Attendance, pk=pk)
		if request.method == 'POST':
			form = AttendanceForm(request.POST, instance=attendance)
			if form.is_valid:
				form.save()
				return redirect('dashboard:attendanceSearch')
		else:
			form = AttendanceForm(instance=attendance)
		return AttendanceView.saveAttendanceForm(request, form, 'attendance/attendancePartialUpdate.html', attendance)

	def saveAttendanceForm(request, form, template_name, attendance):
		html = {}
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