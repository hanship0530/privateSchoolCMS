from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^attendanceInformation/$', views.AttendanceView.searchStudent, name="attendanceSearch"),
    url(r'^attendanceInformation/attendanceList$', views.AttendanceView.getAttendList, name="getAttendList"),

]
