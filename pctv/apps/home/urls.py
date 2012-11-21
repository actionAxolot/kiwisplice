from django.conf.urls import patterns, include, url
from apps.home.views import *


urlpatterns = patterns('', 
	url(r'^login/', LoginView.as_view(), name="login_home"),
        url(r'^dashboard/', DashboardView.as_view(), name="home_dashboard"),
        url(r'^ajax/', HomeAjaxView.as_view(), name="home_ajax"),
	url(r'^$', HomeView.as_view(), name="home_home"),
)
