from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^rosetta/', include('rosetta.urls')),
    (r'^inventario/', include('apps.inventory.urls')),
    (r'^clientes-linea-de-produccion/', include('apps.client.urls')),
    (r'^prospeccion/', include('apps.prospection.urls')),
    (r'^comisiones/', include('apps.commission.urls')),
    (r'^documentos/', include('apps.document.urls')),
    (r'^usuarios/', include('apps.role.urls')),
    (r'^enganche/', include('apps.payment.urls')),
    (r'^logout/$', 'django.contrib.auth.views.logout',
                      {'next_page': '/'}),
    (r'^', include('apps.home.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)
