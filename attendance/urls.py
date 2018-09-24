from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^attendance/$', login_required(views.AttendanceView.searchStudent), name="attendanceSearch"),
    url(r'^attendance/attendanceList/$', login_required(views.AttendanceView.getAttendList), name="getAttendList"),
    url(r'^attendance/(?P<pk>\d+)/update/$', login_required(views.AttendanceView.update), name="attendanceUpdate"),
]
