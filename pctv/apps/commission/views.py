# Create your views here.
from django.views.generic import TemplateView


class CommissionDashboardView(TemplateView):
    template_name = 'commission/index.html'


class CommissionObjectView(TemplateView):
    template_name = 'commission/object_template.html'
