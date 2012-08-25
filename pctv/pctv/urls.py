from django.conf.urls import patterns, include, url
from apps.home.views import CobranzaView, ProspeccionView, InventarioView, ClienteView, CreditoView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pctv.views.home', name='home'),
    # url(r'^pctv/', include('pctv.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^cobranza/', CobranzaView.as_view()),
    (r'^prospeccion/', ProspeccionView.as_view()),
    (r'^inventario/', InventarioView.as_view()),
    (r'^cliente/', ClienteView.as_view()),
    (r'^credito/', CreditoView.as_view()),
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
