from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from apps.client.views import (ClientView, ClientEditView,
    ClientFinancialView, ClientFinancialListView, ClientSalesView,
    ClientDownpaymentView, ClientDashboardView)

urlpatterns = patterns('',
    url(r'^home/$', login_required(ClientView.as_view()), name="client_home"),
    url(r'^ventas/$', login_required(ClientSalesView.as_view()), name="client_sales"),
    url(r'^maduracion-enganche/$', login_required(ClientDownpaymentView.as_view()), name="client_downpayment"),
    url(r'^editar/(?P<client_id>\w+)/', login_required(ClientEditView.as_view()), name="client_edit"),
    url(r'^cobranza/editar/(?P<client_id>\w+)/$', login_required(ClientFinancialView.as_view()), name="client_financial_params"),
    url(r'^cobranza/listar/$', login_required(ClientFinancialListView.as_view()), name="client_financial_list"),
    url(r'^$', login_required(ClientDashboardView.as_view()), name="client_dashboard"),
)
