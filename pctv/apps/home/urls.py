from django.conf.urls import patterns, include, url
from apps.home.views import *


urlpatterns = patterns('', 
	url(r'^login/', LoginView.as_view(), name="login_home"),
	url(r'^$', HomeView.as_view(), name="home_home"),

)