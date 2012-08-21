# Create your views here.
from django.views.generic import TemplateView

class CobranzaView(TemplateView):
	"""Some people just want to watch the world burn"""
	template_name = "home/cobranza.html"


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