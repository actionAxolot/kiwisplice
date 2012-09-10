from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from apps.client.views import ClientView


urlpatterns = patterns('', 
	url(r'^$', login_required(ClientView.as_view()), name="client_home"),
)