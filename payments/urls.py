from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # put your urls
    url(r'^$', login_required(views.PaymentManageView.show), name='managePaymentShow'),
    url(r'^search/$', login_required(views.PaymentManageView.search), name='managePaymentSearch'),  
    url(r'^inquire/$', login_required(views.PaymentManageView.inquire), name='managePaymentInquire'),  
    url(r'^create/$', login_required(views.PaymentManageView.create), name='managePaymentCreate'),
    url(r'^createForm/$', login_required(views.PaymentManageView.createForm), name='managePaymentCreateForm'),     
    url(r'^update/$', login_required(views.PaymentManageView.update), name='managePaymentUpdate'),
    url(r'^updateForm/$', login_required(views.PaymentManageView.updateForm), name='managePaymentUpdateForm'),
    url(r'^delete/$', login_required(views.PaymentManageView.delete), name='managePaymentDelete'),
    url(r'^deleteForm/$', login_required(views.PaymentManageView.deleteForm), name='managePaymentDeleteForm'),    
]
