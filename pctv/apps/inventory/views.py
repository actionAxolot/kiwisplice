# Create your views here.
from django.views.generic import TemplateView


class InventoryView(TemplateView):
	template_name = "inventory/index.html"