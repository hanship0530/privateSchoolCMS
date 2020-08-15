from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(views.AttendanceView.searchStudent), name="attendanceSearch"),
    url(r'^attendanceList/$', login_required(views.AttendanceView.getAttendList), name="getAttendList"),
    url(r'^attendanceList/registerCard/$', login_required(views.AttendanceView.registerCardNumber), name="registerAttendanceCard"),
    url(r'^attendanceList/tagCard/$', login_required(views.AttendanceView.tagStudentAttendance), name="tagAttendanceCard"),
    url(r'^attendanceList/stopTagCard/$', login_required(views.AttendanceView.stopTagStudentAttendance), name="stopTagStudentAttendance"),
    url(r'^(?P<pk>\d+)/update/$', login_required(views.AttendanceView.update), name="attendanceUpdate"),
]
