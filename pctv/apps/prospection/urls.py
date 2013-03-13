from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from apps.prospection.views import (ProspectionView, ProspectionCreateView,
    ProspectionDeleteView, ProspectionDashboardView, ProspectionAjaxView, ProspectionAjaxChannelView,
    ProspectionAjaxStatusView, ProspectionApartarView, ProspectionAuthorizeListView)


urlpatterns = patterns('',
    url(r'^crear/(?P<prospection_id>\w+)/$', login_required(ProspectionCreateView.as_view()), name="prospection_create_params"),
    url(r'^autorizar/$', login_required(ProspectionAuthorizeListView.as_view()), name="prospection_authorize_list_view"),
    url(r'^crear/$', login_required(ProspectionCreateView.as_view()), name="prospection_create"),
    url(r'^borrar/(?P<prospection_id>\w+)/$', login_required(ProspectionDeleteView.as_view()), name="prospection_delete"),
    url(r'^ver/$', login_required(ProspectionView.as_view()), name="prospection_home"),
    url(r'^ajax/channel/$', login_required(ProspectionAjaxChannelView.as_view()), name='prospection_channel_ajax'),
    url(r'^ajax/status/$', login_required(ProspectionAjaxStatusView.as_view()), name='prospection_status_ajax'),
    url(r'^ajax/', login_required(ProspectionAjaxView.as_view()), name='prospection_ajax'),
    url(r'^apartar/', login_required(ProspectionApartarView.as_view()), name='prospection_apartar'),
    url(r'^$', login_required(ProspectionDashboardView.as_view()), name="prospection_dashboard"),
)
