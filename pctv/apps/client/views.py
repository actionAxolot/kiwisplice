# Create your views here.
from django.views.generic import TemplateView


class ClientView(TemplateView):
	template_name = 'client/index.html'