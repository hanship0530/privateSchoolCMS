'''
    urls is to be connect view 
'''
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # manage student urls
    url(r'^student/$', login_required(views.StudentView.display), name="studentDisplay"),
    url(r'^student/create/$', login_required(views.StudentCreateView.create), name='studentCreate'),
    url(r'^student/(?P<pk>\d+)/update/$', login_required(views.StudentView.update), name='studentUpdate'),
    url(r'^student/(?P<pk>\d+)/delete/$', login_required(views.StudentView.delete), name='studentDelete'),
    
    # manage schedule table urls
    url(r'^studentSchedule/$', login_required(views.ScheduleView.display), name='scheduleDisplay'),
    # this is about getting data from web with request.get 
    #url(r'^studentClassSchedule/(?P<pk>\d+)/test/$', views.ClassSchedule.test, name='test'),
    #url(r'^studentClassSchedule/(?P<slug>[-\w]+)/test/$', views.ClassSchedule.test, name='test'),
    url(r'^studentSchedule/updateSchedule/$', login_required(views.ScheduleView.update), name='scheduleUpdate'),
    url(r'^studentSchedule/attendLesson/$', login_required(views.ScheduleView.attendLesson), name='attendLesson'),
    
    # manage student's lesson table urls
    url(r'^lessonTable/$', login_required(views.LessonTableView.displayAttendList), name='lessonTable'),
    url(r'^lessonTable/search/$', login_required(views.LessonTableView.searchStudent), name='lessonTableSearch'),
    url(r'^lessonTable/display/$', login_required(views.LessonTableView.display), name='lessonTableDisplay'),
    url(r'^lessonTable/create/$', login_required(views.LessonTableView.create), name='lessonTableCreate'),
    url(r'^lessonTable/completeFillOut/$', login_required(views.LessonTableView.completeFillout), name='lessonTableFillout'),
    url(r'^lessonTable/update/$', login_required(views.LessonTableView.update), name='lessonTableUpdate'),
    url(r'^lessonTable/selectSheet/$', login_required(views.LessonTableView.getSheet), name='LessonSelectSheet'),
    url(r'^lessonTable/checkPayment/$', login_required(views.LessonTableView.payment), name='lessonTablePayment'),
]
