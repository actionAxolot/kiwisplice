from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from apps.prospection.views import (ProspectionView, ProspectionCreateView, ProspectionDeleteView)


urlpatterns = patterns('',
	url(r'^crear/(?P<prospection_id>\w+)/$', login_required(ProspectionCreateView.as_view()), name="prospection_create_params"),
	url(r'^crear/$', login_required(ProspectionCreateView.as_view()), name="prospection_create"),
	url(r'^borrar/(?P<prospection_id>\w+)/$', login_required(ProspectionDeleteView.as_view()), name="prospection_delete"),
	url(r'^$', login_required(ProspectionView.as_view()), name="prospection_home"),
)