from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from apps.inventory.views import (InventoryView, InventoryCreateView,
    InventoryDeleteView, InventorySectionView,
    InventorySectionCreateView, InventorySectionDeleteView,
    InventoryPrototypeView,
    InventoryPrototypeCreateView, InventoryPrototypeDeleteView,
    InventoryBridgeCreditView,
    InventoryBridgeCreditCreateView, InventoryBridgeCreditDeleteView,
    InventoryDPFView, InventoryDPFDeleteView, InventoryDPFCreateView)


urlpatterns = patterns('',
    # Dashboard
    url(r'^crear/(?P<inventory_id>\w+)/$', login_required(InventoryCreateView.as_view()), {}, name="inventory_create_params"),
    url(r'^crear/$', login_required(InventoryCreateView.as_view()), {}, name="inventory_create"),
    url(r'^borrar/(?P<inventory_id>\w+)/$', login_required(InventoryDeleteView.as_view()), {}, name="inventory_delete"),

    # Prototype
    url(r'^prototipo/$', login_required(InventoryPrototypeView.as_view()), {}, name="inventory_prototype"),
    url(r'^prototipo/crear/(?P<prototype_id>\w+)/$', login_required(InventoryPrototypeCreateView.as_view()), {}, name="inventory_prototype_create_params"),
    url(r'^prototipo/crear/$', login_required(InventoryPrototypeCreateView.as_view()), {}, name="inventory_prototype_create"),
    url(r'^prototipo/borrar/(?P<prototype_id>\w+)/$', login_required(InventoryPrototypeDeleteView.as_view()), {}, name="inventory_prototype_delete"),

    # Section
    url(r'^etapa/$', login_required(InventorySectionView.as_view()), {}, name="inventory_section"),
    url(r'^etapa/crear/(?P<section_id>\w+)/$', login_required(InventorySectionCreateView.as_view()), {}, name="inventory_section_create_params"),
    url(r'^etapa/crear/$', login_required(InventorySectionCreateView.as_view()), {}, name="inventory_section_create"),
    url(r'^etapa/borrar/(?P<section_id>\w+)/$', login_required(InventorySectionDeleteView.as_view()), {}, name="inventory_section_delete"),

    # Bridge Credits
    url(r'^credito-puente/$', login_required(InventoryBridgeCreditView.as_view()), {}, name="inventory_bridge_credit"),
    url(r'^credito-puente/crear/$', login_required(InventoryBridgeCreditCreateView.as_view()), {}, name="inventory_bridge_credit_create"),
    url(r'^credito-puente/crear/(?P<bridge_credit_id>\w+)/$', login_required(InventoryBridgeCreditCreateView.as_view()), {}, name="inventory_bridge_credit_create_params"),
    url(r'^credito-puente/borrar/(?P<bridge_credit_id>\w+)/$', login_required(InventoryBridgeCreditDeleteView.as_view()), {}, name="inventory_bridge_credit_delete"),

    # DPF
    url(r'^dpf/$', login_required(InventoryDPFView.as_view()), {}, name="inventory_dpf"),
    url(r'^dpf/crear/$', login_required(InventoryDPFCreateView.as_view()), {}, name="inventory_dpf_create"),
    url(r'^dpf/crear/(?P<dpf_id>\w+)/$', login_required(InventoryDPFCreateView.as_view()), {}, name="inventory_dpf_create_params"),
    url(r'^dpf/borrar/(?P<dpf_id>\w+)/$', login_required(InventoryDPFCreateView.as_view()), {}, name="inventory_dpf_delete"),

    # Fallback
    url(r'^$', login_required(InventoryView.as_view()), {}, name="inventory_home"),
)
