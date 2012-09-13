from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from apps.inventory.views import InventoryView, InventoryCreateView, InventoryDeleteView


urlpatterns = patterns('', 
	url(r'^crear/(?P<inventory_id>\w+)/$', login_required(InventoryCreateView.as_view()), {}, name="inventory_create_params"),
	url(r'^crear/$', login_required(InventoryCreateView.as_view()), {}, name="inventory_create"),
	url(r'^borrar/(?P<inventory_id>\w+)/$', login_required(InventoryDeleteView.as_view()), {}, name="inventory_delete"),
	url(r'^$', login_required(InventoryView.as_view()), {}, name="inventory_home"),
)