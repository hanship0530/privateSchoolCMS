from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.LoginView.as_view(), name="login"),
    url(r'^index/$', views.IndexView.as_view(), name="index"),
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

    # 내가 커스텀마이징 한 부분
    # 대시보드 뷰에서 만든 부분을 대시보드 url에서 연결
    url(r'^students/', include('students.urls')),
    url(r'^attendance/', include('attendance.urls')),
    url(r'^payment/', include('payments.urls')),
]
