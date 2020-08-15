from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(views.AttendanceView.searchStudent), name="attendanceSearch"),
    url(r'^attendanceList/$', login_required(views.AttendanceView.getAttendList), name="getAttendList"),
    url(r'^(?P<pk>\d+)/update/$', login_required(views.AttendanceView.update), name="attendanceUpdate"),
]
