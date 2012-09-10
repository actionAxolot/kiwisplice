from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from apps.prospection.views import ProspectionView, ProspectionCreateView


urlpatterns = patterns('',
	url(r'^crear/', login_required(ProspectionCreateView.as_view()), name="prospection_create"),
	url(r'^$', login_required(ProspectionView.as_view()), name="prospection_home"),
)