from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from apps.client.views import *

urlpatterns = patterns('',
    url(r'^ventas/$', login_required(ClientSalesView.as_view()), name="client_sales"),
    url(r'^editar/(?P<client_id>\w+)/', login_required(ClientEditView.as_view()), name="client_edit"),
    url(r'^cobranza/editar/(?P<client_id>\w+)/$', login_required(ClientFinancialView.as_view()), name="client_financial_params"),
    url(r'^cobranza/listar/$', login_required(ClientFinancialListView.as_view()), name="client_financial_list"),
    url(r'^regresar-a-prospeccion/(?P<client_id>\w+)/$', login_required(ClientReturnToProspectionView.as_view()), name="client_to_prospection"),
    url(r'^dashboard/$', login_required(ClientDashboardView.as_view()), name="client_dashboard"),
    url(r'^ajax/$', login_required(ClientAjaxView.as_view()), name="client_ajax"),
    url(r'^$', login_required(ClientView.as_view()), name="client_home"),
)
