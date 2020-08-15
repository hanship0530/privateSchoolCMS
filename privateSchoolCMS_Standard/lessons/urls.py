from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # put your urls
    url(r'^manageLesson/$', login_required(views.LessonManageView.show), name="manageLessonShow"),
    url(r'^manageLesson/create/$', login_required(views.LessonCreateView.create), name="manageLessonCreate"),
    url(r'^manageLesson/(?P<pk>\d+)/update/$', login_required(views.LessonManageView.update), name='manageLessonUpdate'),
    url(r'^manageLesson/(?P<pk>\d+)/delete/$', login_required(views.LessonManageView.delete), name='manageLessonDelete'),
    url(r'^managePayment/student/(?P<pk>\d+)/inquire/$', login_required(views.LessonManageView.inquire), name='managePaymentStudentInquire'),
    url(r'^managePayment/student/(?P<pk>\d+)/delete/$', login_required(views.LessonManageView.deleteStudentLesson), name='managePaymentStudentDelete'),     
]
