'''
	admin urls
'''
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	#admin에서 include로 바로 넘기기에 로그인 기능등 모든 기능은 dashboard에서 이루어져야 함
    url(r'^', include('dashboard.urls', namespace='dashboard')),
    url(r'^admin/', include(admin.site.urls)),
]
