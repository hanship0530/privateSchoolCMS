'''
    2018-08-02
    Student Information CRUD, Making lesson table

    Made by Han
'''
from django.views.generic import TemplateView

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Student
from attendance.models import Attendance
from .forms import StudentForm
from .schedule_func import sunday, monday, tuseday, wendsday, thursday, friday, saturday
from .lessonTable_func import update_excelsheet, display_excelsheet
import win32com.client, datetime, pythoncom, os, re, openpyxl
from django.utils import timezone
# manage student 
class StudentView(TemplateView): 
    def display(request):
        students = Student.objects.all()
        # paginator = Paginator(student_list, 5)
        # page = request.GET.get('page')
        # print("Student List Out Code")
        # try:
        #     students = paginator.page(page)
        # except PageNotAnInteger:
        #     students = paginator.page(1)
        # except EmptyPage:
        #     students = paginator.page(paginator.num_pages)
        return render(request, 'student/student.html', {'students' : students})
    def saveStudentForm(request, form, template_name, student):
        html = {}
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                html['form_is_valid'] = True
                students = Student.objects.all()
                html['studentList'] = render_to_string('student/studentPartialList.html', {
                'students': students
                })           
            else:
                html['form_is_valid'] = False
        context = {'form':form,'student':student}
        html['html_form'] = render_to_string(template_name, context, request=request)           
        return JsonResponse(html)
    def update(request):
        if request.method == 'POST':
            number = request.POST['number']
            student = Student.objects.get(number=number)
            form = StudentForm(instance=student)
            return StudentView.saveStudentForm(request, form, 'student/studentPartialUpdate.html', student)
    def updateForm(request):
        if request.method == 'POST':
            number = request.POST['number']
            student = Student.objects.get(number=number)
            form = StudentForm(request.POST, instance=student)
            return StudentView.saveStudentForm(request, form, 'student/studentPartialUpdate.html',student)
    def deleteForm(request):
        html = {}
        if request.method == 'POST':
            number = request.POST['number']
            student = Student.objects.get(number=number)
            student.delete()
            html['form_is_valid'] = True
            students = Student.objects.all()
            html['studentList'] = render_to_string('student/studentPartialList.html', 
                {'students': students })
            return JsonResponse(html)
    def delete(request):
        html={}
        if request.method=='POST':
            print(request.POST)
            number = request.POST['number']
            student = Student.objects.get(number=number)
            context = {'student':student,'student':student}
            html['html_form'] = render_to_string('student/studentPartialDelete.html', context,request=request)
            return JsonResponse(html)

# create student
class StudentCreateView(TemplateView):      
    def create(request):
        if request.method == 'POST':
            form = StudentForm(request.POST)
            return StudentCreateView.saveStudentForm(request, form, 'student/studentPartialCreate.html')  
        else:
            number = Student.objects.all().count() + 1
            form = StudentForm(initial={'number':number}) 
            return render(request, 'student/studentCreate.html', {'form':form})
    def saveStudentForm(request, form, template_name):
        html = {}
        if request.method == 'POST':
            if form.is_valid():
                html['form_is_valid'] = True
                form.save()
                form = StudentForm()
            else:
                html['form_is_valid'] = False   
        context = {'form':form}
        html['form_html'] = render_to_string(template_name, context, request=request)        
        return JsonResponse(html)               


# class time schedule
class ScheduleView(TemplateView):
    def getData(day, sheetName, filepath):
        scheduleData = []
        if(day==1): # Monday
            scheduleData = monday(filepath, sheetName, day)                                       
        elif(day==2): # Tuseday
            scheduleData = tuseday(filepath, sheetName, day)            
        elif(day==3):  # Wendsday
            scheduleData = wendsday(filepath, sheetName, day) 
        elif(day==4):  # Thursday
            scheduleData = thursday(filepath, sheetName, day) 
        elif(day==5):  # Friday
            scheduleData = friday(filepath, sheetName, day) 
        elif(day==6):  # Saturday
            scheduleData = saturday(filepath, sheetName, day) 
        elif(day==7):  # Sunday
            scheduleData = sunday(filepath, sheetName, day)
        return scheduleData

    def display(request):
        html = {}
        if "GET" == request.method:
            return render(request,'scheduleTable/scheduleTable.html',{})
        else:
            # can get data from <form> html with request.POST way
            daymonthyear = request.POST
            date = daymonthyear['daymonthyear'].split(' ')
            dayTuple = datetime.datetime(int(date[2]),int(date[1]),int(date[0])).isocalendar()
            day = dayTuple[2]
            sheetName = str(dayTuple[0])+'년_'+str(dayTuple[1])+'주차'
            filepath = request.user.profile.fileName
            scheduleData = ScheduleView.getData(day, sheetName, filepath)
            html['scheduleTable'] = render_to_string('scheduleTable/scheduleTableList.html', {"scheduleTable":scheduleData}, 
                request=request)
            return JsonResponse(html) 
    
    def update(request):
        if request.method == 'POST':
            try:
                html = dict()
                cells = request.POST['cellInfo'].split("/")
                filepath = request.user.profile.fileName
                # Open Excel 
                pythoncom.CoInitialize()
                excel = win32com.client.DispatchEx('Excel.Application')
                workbook = excel.Workbooks.Open(os.path.join(os.getcwd(), filepath))
                excel.Visible = False
                excel.DisplayAlerts = False            
                worksheet = workbook.Worksheets(request.POST['sheet'])
                worksheet.Range(cells[0]).Value = request.POST['number']
                worksheet.Range(cells[1]).Value = request.POST['name']
                worksheet.Range(cells[2]).Value = request.POST['grade']
                worksheet.Range(cells[3]).Value = request.POST['memo']
                workbook.Save()
                workbook.Close(True)
                excel.Application.Quit()
                # Close Excel 
                
                scheduleData = ScheduleView.getData(int(request.POST['day']), request.POST['sheet'], filepath)
                html['is_valid'] = True
                html['scheduleTable'] = render_to_string('scheduleTable/scheduleTableList.html', {"scheduleTable":scheduleData}, 
                request=request)
                return JsonResponse(html)
            except Exception as e:
                print("Error: "+str(e))
                html['is_valid'] = False
                html['errorMsg'] = "Error: "+str(e)
                return JsonResponse(html)   
    def attendLesson(request):
        if request.method == 'POST':
            html = {}
            try:
                student = Student.objects.get(number=request.POST['number'])
                date = timezone.localtime(timezone.now()).date()
                today = Attendance(attendanceDate=date, student=student)
                # attend_list = student.attendance_set.all()
                isAttend = student.attendance_set.filter(attendanceDate=date, student=student)
                if not isAttend: 
                    today.save()
                    student.attendance_set.add(today)
                    html['is_valid'] = True
                    html['scheduleTable'] = str(student.stname)+"("+str(student.number)+")"+" 의출석이 정상적으로 되었습니다."
                    return JsonResponse(html)                 
                else:
                    html['is_valid'] = False
                    html['errorMsg'] = str(student.stname)+"("+str(student.number)+")"+" 이미 출석했습니다." 
                    return JsonResponse(html)
            except Exception as e:
                print("Error: "+str(e))
                html['is_valid'] = False
                html['errorMsg'] = "Error: "+str(e)
                return JsonResponse(html)  
    # Get request with ajax    
    # def httpGetWay(request,slug):
    #     print("test")
    #     chart = get_object_or_404(pk=slug)
    #     print("slug: ")
    #     print(slug)
    #     print("chart: ")    
    #     print(chart)
    #     testing = dict()
    #     return render(request, 'components/studentClassScheduleTable.html', {"schedule_data":testing})



# manage student's lesson table
class LessonTableView(TemplateView):
    def displayAttendList(request):
        today = timezone.localtime(timezone.now()).date()
        # 오늘 출석한 회원 리스트 얻기
        if Attendance.objects.filter(attendanceDate=today).exists():
            student_list = Attendance.objects.filter(attendanceDate=today, fillOut='미작성')
            students = []
            # html출력 형식으로 인한 데이터 전처리
            for student in student_list:
                students.append(student.student)
            return render(request, "lessonTable/lessonTable.html", {'students' : students})
        else: # 출석한 회원이 없는 경우
            return render(request, "lessonTable/lessonTable.html", {})
        
    def searchStudent(request):
        try:
            html= {}
            if request.method == 'POST':
                name = request.POST['name']
                student_list = Student.objects.filter(stname=name)
                students = []
                # html출력 형식으로 인한 데이터 전처리
                for student in student_list:
                    students.append(student) 
                html['is_valid'] = True
                # 출력할 html 형식을 render_to_string을 통해 보내 html형식을 받아옴   
                html['studentList'] = render_to_string("lessonTable/lessonTableStudentList.html", {'students':students},
                    request=request)
                html['lessonList'] = render_to_string("lessonTable/lessonTableList.html", {},
                    request=request)                
            else: # 아무 요청도 없을 경우 
                html['is_valid'] = True
                html['studentList'] = render_to_string("lessonTable/lessonTableStudentList.html", {}, request=request)
                html['lessonList'] = render_to_string("lessonTable/lessonTableList.html", {}, request=request)   
            return JsonResponse(html) 
        except Exception as e:
            print("Error: "+str(e))
            html['is_valid'] = False
            html['errorMsg'] = "Errors: "+str(e)
            return JsonResponse(html)

    def create(request):
        html = {}
        try:
            if request.method == 'POST':
                number = request.POST['number']
                student = Student.objects.get(number=number)
                sheetName = str(timezone.localtime(timezone.now()).date())
                student.sheet = sheetName
                student.save()
                
                # Open Excel
                pythoncom.CoInitialize()
                excel = win32com.client.DispatchEx('Excel.Application')
                filepath = os.path.join(os.getcwd(),student.filepath)
                workbook = excel.Workbooks.Open(filepath)
                excel.Visible = False
                excel.DisplayAlerts = False

                worksheet1 = workbook.Worksheets("main")
                worksheet2 = workbook.Worksheets.Add()
                worksheet2.Name = sheetName
                worksheet2 = workbook.Worksheets(sheetName)
                worksheet1.Range("A1:AF100").Copy(worksheet2.Range("A1:AH41"))
                worksheet2.Range("E5").Value = str(student.stname)
                worksheet2.Range("E5").Font.Size = 12
                worksheet2.Range("C9").Value = str(student.number)
                worksheet2.Range("C9").Font.Size = 12
                worksheet2.Range("C10").Value = str(student.dateOfBirth)
                worksheet2.Range("C10").Font.Size = 12
                worksheet2.Range("C11").Value = str(student.dateOfEnroll)
                worksheet2.Range("C11").Font.Size = 12
                worksheet2.Range("E10").Value = str(student.years)+'/'+str(student.gender)
                worksheet2.Range("E10").Font.Size = 12
                worksheet2.Range("E11").Value = str(student.school)
                worksheet2.Range("E11").Font.Size = 8
                worksheet2.Range("G10").Value = str(student.contact)
                worksheet2.Range("G10").Font.Size = 12

                workbook.Save()
                workbook.Close(True)
                excel.Application.Quit()
                # Close Excel
                
                students = Student.objects.filter(stname=student.stname)

                html['is_valid'] = True
                html['studentList'] = render_to_string("lessonTable/lessonTableStudentList.html", {'students':students},
                    request=request)
                return JsonResponse(html) 
        except Exception as e:
            print("Error: "+str(e))
            html['is_valid'] = False
            html['errorMsg'] = "Error: "+str(e)
            student.sheet = "main"
            return JsonResponse(html) 
    
    def display(request):
        html = {}
        today = timezone.localtime(timezone.now()).date()
        if request.method == 'POST':
            try:
                number = request.POST['number']
                student = Student.objects.get(number=number)
                wb = openpyxl.load_workbook(os.path.join(os.getcwd(),student.filepath))
                if student.sheet != "main":
                    student.sheet = wb.sheetnames[-1]
                    tableData = display_excelsheet(student.filepath, student.sheet)
                    html['is_valid'] = True
                    html['is_main'] = False
                    html['lessonTable'] = render_to_string("lessonTable/lessonTableList.html", {'table':tableData[0:-2]},
                        request=request)
                    html['student'] = {'name':student.stname, 'number':student.number}
                    html['worksheets'] = render_to_string("lessonTable/lessonTableSelect.html", {'worksheets':tableData[-1]})
                    html['message'] = "Successfully completed."
                else:
                    student.sheet = wb.sheetnames[-1]
                    tableData = display_excelsheet(student.filepath, student.sheet)
                    html['is_valid'] = True
                    html['is_main'] = True
                    html['lessonTable'] = render_to_string("lessonTable/lessonTableList.html", {},
                        request=request)
                    html['student'] = {'name':student.stname, 'number':student.number}
                    html['worksheets'] = render_to_string("lessonTable/lessonTableSelect.html", {'worksheets':tableData[-1]})
                    html['message'] = "차트가 생성이 안되었습니다. 생성버튼을 눌러 엑셀 시트를 생성해주세요."
                return JsonResponse(html)
            except Exception as e:
                print("Error: "+str(e))
                html['is_valid'] = False
                html['errorMsg'] = "Errors: "+str(e)
                return JsonResponse(html)

    def completeFillout(request):
        html = {}
        today = timezone.localtime(timezone.now()).date()

        if request.method == 'POST':
            try:
                student = Student.objects.get(number=request.POST['number'])
                attend = Attendance.objects.get(attendanceDate=today, student=student, fillOut='미작성')
                attend.fillOut = True
                attend.save()
                html['is_valid'] = True
                students = Student.objects.filter(stname=student.stname)
                html['studentList'] = render_to_string("lessonTable/lessonTableStudentList.html", {'students':students},
                    request=request)                
                return JsonResponse(html)
            except Exception as e:
                print("Error: "+str(e))
                html['is_valid'] = False
                html['errorMsg'] = "Error: "+str(e)
                return JsonResponse(html)


    def update(request):
        html = {}
        if request.method == 'POST':
            try:
                tableData = {}
                cells = request.POST['cells']
                number = int(str(request.POST['number']).split('(')[1].split(')')[0])
                sheetName = request.POST['sheetName']
                cells = cells.split('/')
                student = Student.objects.get(number=number)
                students = Student.objects.filter(stname=student.stname)
                tableData['date'] = request.POST['date']
                tableData['content'] = request.POST['content']
                tableData['completed'] = request.POST['completed']
                tableData['memo'] = request.POST['memo']

                update_excelsheet(student.filepath, sheetName, tableData, cells) 
                datafordisplay = display_excelsheet(student.filepath,sheetName)
                html['is_valid'] = True
                html['studentList'] = render_to_string("lessonTable/lessonTableStudentList.html", {'students':students},
                    request=request)                 
                html['lessonTable'] = render_to_string("lessonTable/lessonTableList.html", {'table':datafordisplay[0:-2]}
                    , request=request)
                html['worksheets'] = datafordisplay[-1]
                return JsonResponse(html)
            except Exception as e:
                print("Error: "+str(e))
                html['is_valid'] = False
                html['errorMsg'] = "Error: "+str(e)
                return JsonResponse(html) 

    def getSheet(request):
        html = {}
        if request.method == 'POST':
            try:
                number = int(request.POST['number'].split('(')[1].split(')')[0])
                sheetName = request.POST['sheet']
                student = Student.objects.get(number=number)
                students = Student.objects.filter(stname=student.stname)
                tables = display_excelsheet(student.filepath, sheetName)
                html['is_valid'] = True
                html['lessonTables'] = render_to_string("lessonTable/lessonTableList.html", {'table':tables[0:-2]}
                    , request=request)
                html['worksheet'] = tables[-1]
                html['studentNumber'] = number
                html['studentList'] = render_to_string("lessonTable/lessonTableStudentList.html", {'students':students})
            except Exception as e:
                print("Error: ", str(e))
                html['is_valid'] = False
                html['errorMsg'] = "Error: " + str(e)
            return JsonResponse(html)
    def payment(request):
        html = {}
        if request.method == 'POST':
            try:
                number = int(request.POST['number'])
                student = Student.objects.get(number=number)
                student.isPayday = 'PAY'
                student.save()
                students = Student.objects.filter(stname=student.stname)
                html['is_valid'] = True
                html['studentList'] = render_to_string("lessonTable/lessonTableStudentList.html", {'students':students}, request=request)
            except Exception as e:
                print("Error: ", str(e))
                html['is_valid'] = False
                html['errorMsg'] = "Error: " + str(e)
            return JsonResponse(html)

