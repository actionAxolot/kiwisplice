from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from views import *

urlpatterns = patterns('',
    url(r'^dashboard/$', login_required(PaymentView.as_view()), name="payment_dashboard"),
    url(r'^$', login_required(PaymentDashboard.as_view()), name="payment_index"),
)
