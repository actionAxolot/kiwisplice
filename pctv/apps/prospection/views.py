# Create your views here.
from django.views.generic import (ListView, DetailView,
	DeleteView, CreateView, TemplateView)
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect

from models import Prospection
from apps.client.models import Client
from forms import ProspectionForm, PhoneNumberForm, ProspectionPhoneNumberFormset


class ProspectionView(ListView):
	model = Prospection
	queryset = Prospection.objects.all().exclude(status__in=("Apartado"))
	template_name = "prospection/index.html"


class ProspectionCreateView(TemplateView):
	template_name = "prospection/new_form.html"


	def post(self, request, prospection_id=None):
		prospection = Prospection()
		if prospection_id:
			prospection = Prospection.objects.get(pk=prospection_id)

		prospection_form = ProspectionForm(request.POST, request.FILES, instance=prospection)

		if prospection_form.is_valid():
			created_prospection = prospection_form.save()
			if created_prospection.status in ("Apartado", "Por cerrar",):
				try:
					client = Client.objects.get(prospection=created_prospection)
				except Client.DoesNotExist:
					client = Client(prospection=prospection)
					client.save()
		else:
			created_prospection = Prospection()

		inline_formset = ProspectionPhoneNumberFormset(request.POST, instance=created_prospection)

		if inline_formset.is_valid():
			inline_formset.save()

			if created_prospection.status in ("Apartado", "Por cerrar"):
				return redirect("client_edit", client_id=created_prospection.client_set.all()[0].pk)
			else:
				return redirect("prospection_home")

		return self.render_to_response({
			"form": prospection_form,
			"formset": inline_formset
		})


	def get(self, request, prospection_id=None):
		if prospection_id:
			prospection = Prospection.objects.get(pk=prospection_id)
			prospection_form = ProspectionForm(instance=prospection)
		else:
			prospection = Prospection()
			prospection_form = ProspectionForm()

		inline_formset = ProspectionPhoneNumberFormset(instance=prospection)
		return self.render_to_response({
			"form": prospection_form,
			"formset": inline_formset,
		})


class ProspectionDeleteView(TemplateView):
	def get(self, request, prospection_id=None):
		Prospection.objects.get(pk=prospection_id).delete()
		return redirect("prospection_home")
	