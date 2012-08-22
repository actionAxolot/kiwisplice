# Create your views here.
from django.views.generic import TemplateView
from django.conf import settings

class CobranzaView(TemplateView):
	"""Some people just want to watch the world burn"""
	template_name = "home/cobranza.html"

	def get_context_data(self, **kwargs):
		return {'media_path': settings.MEDIA_ROOT, 'static_path': settings.STATIC_ROOT}


class ProspeccionView(TemplateView):
	"""I'm Gotham's reckoning"""
	template_name = "home/prospeccion.html"


class InventarioView(TemplateView):
	"""I'm in lesbians with you"""
	template_name = "home/inventario.html"


class ClienteView(TemplateView):
	"""I'm in lesbians with you"""
	template_name = "home/cliente.html"


class CreditoView(TemplateView):
	"""I'm in lesbians with you"""
	template_name = "home/credito.html"