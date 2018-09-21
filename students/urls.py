'''
    urls is to be connect view 
'''
from django.conf.urls import url
from . import views

urlpatterns = [
    # manage student urls
    url(r'^student/$', views.StudentView.display, name="studentDisplay"),
    url(r'^student/create/$', views.StudentCreateView.create, name='studentCreate'),
    url(r'^student/(?P<pk>\d+)/update/$', views.StudentView.update, name='studentUpdate'),
    url(r'^student/(?P<pk>\d+)/delete/$', views.StudentView.delete, name='studentDelete'),
    
    # manage schedule table urls
    url(r'^studentSchedule/$', views.ScheduleView.display, name='scheduleDisplay'),
    # this is about getting data from web with request.get 
    #url(r'^studentClassSchedule/(?P<pk>\d+)/test/$', views.ClassSchedule.test, name='test'),
    #url(r'^studentClassSchedule/(?P<slug>[-\w]+)/test/$', views.ClassSchedule.test, name='test'),
    url(r'^studentSchedule/updateSchedule/$', views.ScheduleView.update, name='scheduleUpdate'),
    url(r'^studentSchedule/attendLesson/$', views.ScheduleView.attendLesson, name='attendLesson'),
    
    # manage student's lesson table urls
    url(r'^lessonTable/$', views.LessonTableView.displayAttendList, name='lessonTable'),
    url(r'^lessonTable/search/$', views.LessonTableView.searchStudent, name='lessonTableSearch'),
    url(r'^lessonTable/display/$', views.LessonTableView.display, name='lessonTableDisplay'),
    url(r'^lessonTable/create/$', views.LessonTableView.create, name='lessonTableCreate'),
    url(r'^lessonTable/completeFillOut/$', views.LessonTableView.completeFillout, name='lessonTableFillout'),
    url(r'^lessonTable/update/$', views.LessonTableView.update, name='lessonTableUpdate'),
    url(r'^lessonTable/selectSheet/$', views.LessonTableView.getSheet, name='LessonSelectSheet'),
]
