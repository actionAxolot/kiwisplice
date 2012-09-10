from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from apps.inventory.views import InventoryView


urlpatterns = patterns('', 
	url(r'^$', login_required(InventoryView.as_view()), {}, name="inventory_home"),
)