from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # put your urls
    url(r'^manageLesson/$', login_required(views.LessonManageView.show), name="manageLessonShow"),
    url(r'^manageLesson/create/$', login_required(views.LessonCreateView.create), name="manageLessonCreate"),
    url(r'^manageLesson/(?P<pk>\d+)/update/$', login_required(views.LessonManageView.update), name='manageLessonUpdate'),
    url(r'^manageLesson/(?P<pk>\d+)/delete/$', login_required(views.LessonManageView.delete), name='manageLessonDelete'),
    url(r'^managePayment/$', login_required(views.PaymentManageView.show), name='managePaymentShow'),
    url(r'^managePayment/search/$', login_required(views.PaymentManageView.search), name='managePaymentSearch'),  
    url(r'^managePayment/(?P<pk>\d+)/inquire/$', login_required(views.PaymentManageView.inquire), name='managePaymentInquire'),  
    url(r'^managePayment/(?P<pk>\d+)/create/$', login_required(views.PaymentManageView.create), name='managePaymentCreate'),
    url(r'^managePayment/createForm/$', login_required(views.PaymentManageView.createForm), name='managePaymentCreateForm'),     
    url(r'^managePayment/(?P<pk>\d+)/update/$', login_required(views.PaymentManageView.update), name='managePaymentUpdate'),
    url(r'^managePayment/(?P<pk>\d+)/delete/$', login_required(views.PaymentManageView.delete), name='managePaymentDelete'),    
]
