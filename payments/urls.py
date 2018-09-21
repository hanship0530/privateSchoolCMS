from django.conf.urls import url
from . import views

urlpatterns = [
    # put your urls
    url(r'^manageLesson/$', views.LessonManageView.show, name="manageLessonShow"),
    url(r'^manageLesson/create/$', views.LessonCreateView.create, name="manageLessonCreate"),
    url(r'^manageLesson/(?P<pk>\d+)/update/$', views.LessonManageView.update, name='manageLessonUpdate'),
    url(r'^manageLesson/(?P<pk>\d+)/delete/$', views.LessonManageView.delete, name='manageLessonDelete'),
    url(r'^managePayment/$', views.PaymentManageView.show, name='managePaymentShow'),
    url(r'^managePayment/search/$', views.PaymentManageView.search, name='managePaymentSearch'),  
    url(r'^managePayment/(?P<pk>\d+)/inquire/$', views.PaymentManageView.inquire, name='managePaymentInquire'),  
    url(r'^managePayment/(?P<pk>\d+)/create/$', views.PaymentManageView.create, name='managePaymentCreate'),
    url(r'^managePayment/createForm/$', views.PaymentManageView.createForm, name='managePaymentCreateForm'),   
    url(r'^managePayment/(?P<pk>\d+)/update/$', views.PaymentManageView.update, name='managePaymentUpdate'),
    url(r'^managePayment/(?P<pk>\d+)/delete/$', views.PaymentManageView.delete, name='managePaymentDelete'),    
]
