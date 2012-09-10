from django.conf.urls import patterns, include, url
from apps.home.views import HomeView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pctv.views.home', name='home'),
    # url(r'^pctv/', include('pctv.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^rosetta/', include('rosetta.urls')),
    # Uncomment the next line to enable the admin:
    (r'^inventario/', include('apps.inventory.urls')),
    (r'^clientes-linea-de-produccion/', include('apps.client.urls')),
    (r'^prospeccion/', include('apps.prospection.urls')),
    (r'^comisiones/', include('apps.commission.urls')),
    # (r'^grappelli/', include('grappelli.urls')),
    (r'^', include('apps.home.urls')),
)
