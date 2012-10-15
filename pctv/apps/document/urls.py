from django.conf.urls import patterns, url
from views import DocsView

urlpatterns = patterns('',
     url(r"^$", DocsView.as_view(), {}, name="documentacion"),
)
