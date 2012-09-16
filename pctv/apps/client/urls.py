from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from apps.client.views import (ClientView, ClientEditView, 
	ClientFinancialView, ClientFinancialListView, ClientSalesView, ClientDownpaymentView)


urlpatterns = patterns('', 
	url(r'^$', login_required(ClientView.as_view()), name="client_home"),
	url(r'^ventas/$', login_required(ClientSalesView.as_view()), name="client_sales"),
	url(r'^maduracion-enganche/$', login_required(ClientDownpaymentView.as_view()), name="client_downpayment"),
	url(r'^editar/(?P<client_id>\w+)/', login_required(ClientEditView.as_view()), name="client_edit"),
	url(r'^cobranza/editar/(?P<client_id>\w+)/$', login_required(ClientFinancialView.as_view()), name="client_financial_params"),
	url(r'^cobranza/listar/$', login_required(ClientFinancialListView.as_view()), name="client_financial_list"),
)