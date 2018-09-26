'''
    urls is to be connect view 
'''
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # manage student urls
    url(r'^display/$', login_required(views.daySalesView.display), name="salesDisplay"),
    url(r'^display/makeDay/$', login_required(views.daySalesView.makeDay), name='salesCreateDay'),
    url(r'^display/inquire/$', login_required(views.daySalesView.inquire), name='salesInquire'),
    url(r'^display/monthSales/$', login_required(views.motnthSaleView.as_view()), name='monthSales'),
]
