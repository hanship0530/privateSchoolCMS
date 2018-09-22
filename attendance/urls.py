from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^attendanceInformation/$', login_required(views.AttendanceView.searchStudent), name="attendanceSearch"),
    url(r'^attendanceInformation/attendanceList$', login_required(views.AttendanceView.getAttendList), name="getAttendList"),

]
