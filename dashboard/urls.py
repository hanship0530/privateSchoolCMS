from django.conf.urls import url, include
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # sb-admin components urls
    url(r'^blank/$', views.BlankView.as_view(), name="blank"),
    url(r'^buttons/$', views.ButtonsView.as_view(), name="buttons"),
    url(r'^flot/$', views.FlotView.as_view(), name="flot"),
    url(r'^forms/$', views.FormsView.as_view(), name="forms"),
    url(r'^grid/$', views.GridView.as_view(), name="grid"),
    url(r'^icons/$', views.IconsView.as_view(), name="icons"),
    url(r'^morris/$', views.MorrisView.as_view(), name="morris"),
    url(r'^notifications/$', views.NotificationsView.as_view(), name="notifications"),
    url(r'^panels/$', views.PanelsView.as_view(), name="panels"),
    url(r'^tables/$', views.TablesView.as_view(), name="tables"),
    url(r'^typography/$', views.TypographyView.as_view(), name="typography"),

    # app urls
    url(r'^$', auth_views.login, {'template_name': 'components/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'components/logout.html'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^setting/$', views.setting, name='setting'),
    url(r'^index/$', login_required(views.IndexView.as_view()), name="index"),    
    url(r'^create/$', login_required(views.NoticeView.create), name='noticeCreate'),
    url(r'^delete/$', login_required(views.NoticeView.deleteButton), name='noticeDelete'),
    url(r'^delete2/$', login_required(views.NoticeView.deleteForm), name='noticeDelete2'),
    url(r'^createPayment/$', login_required(views.DashPaymentView.createPayment), name='dashboardPayment'),
    url(r'^createPayment/Form/$', login_required(views.DashPaymentView.createPaymentForm), name='dashboardPaymentCreate'),    
    url(r'^error/$', login_required(views.ErrorView.as_view()), name='error'),

    url(r'^students/', include('students.urls')),
    url(r'^attendance/', include('attendance.urls')),
    url(r'^payments/', include('payments.urls')),
    url(r'^lessons/', include('lessons.urls')),
    url(r'^sales/', include('sales.urls')),
]
