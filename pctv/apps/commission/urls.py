from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from apps.commission.views import CommissionView

urlpatterns = patterns('',
	url(r'^$', login_required(CommissionView.as_view()), name="commission_home"),
)