# Create your views here.
from django.views.generic import TemplateView


class CommissionView(TemplateView):
	template_name = 'commission/index.html'