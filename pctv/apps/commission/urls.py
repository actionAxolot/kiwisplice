from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from apps.commission.views import *

urlpatterns = patterns('',
      url(r'^$', login_required(CommissionDashboardView.as_view()), name="commission_dashboard"),
      url(r'^ajax/$', login_required(CommissionAjaxView.as_view()), name="commission_ajax"),
      url(r'^pagos/(\d+)/$', login_required(CommissionPaymentView.as_view()), name="commission_payment")
)
