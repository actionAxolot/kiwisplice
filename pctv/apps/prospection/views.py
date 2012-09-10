# Create your views here.
from django.views.generic import (ListView, DetailView,
	DeleteView, CreateView)
from django.core.urlresolvers import reverse_lazy

from models import Prospection


class ProspectionView(ListView):
	model = Prospection
	template_name = "prospection/index.html"


class ProspectionCreateView(CreateView):
	template_name = "prospection/new_form.html"
	success_url = reverse_lazy("prospection_home")
	model = Prospection


class ProspectionDetailView(DetailView):
	pass


class ProspectionDeleteView(DeleteView):
	pass