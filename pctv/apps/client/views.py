# Create your views here.
from django.views.generic import TemplateView, ListView
from django.shortcuts import redirect

from models import Client
from forms import ClientPaymentFormSet, ClientForm


class ClientView(ListView):
	template_name = 'client/index.html'
	model = Client


class ClientEditView(TemplateView):
	template_name = 'client/new_form.html'


	def get(self, request, client_id=None):
		"""
		Render the forms and whatnot
		"""
		if client_id:
			client = Client.objects.get(pk=client_id)
			client_form = ClientForm(instance=client)
		else:
			client = Client()
			client_form = ClientForm(instance=client)

		inline_formset = ClientPaymentFormSet(instance=client)

		return self.render_to_response({
			"form": client_form,
			"formset": inline_formset,
			"client": client
		})


	def post(self, request, client_id=None):
		"""
		Save the form and create relevant records
		"""
		client = Client()
		if client_id:
			client = Client.objects.get(pk=client_id)

		client_form = ClientForm(request.POST, request.FILES, instance=client)

		if client_form.is_valid():
			created_client = client_form.save()
			inline_formset = ClientPaymentFormSet(request.POST, 
				request.FILES, instance=created_client)
			if inline_formset.is_valid():
				inline_formset.save()
			return redirect("client_home")
		else:
			inline_formset = ClientPaymentFormSet(request.POST, request.FILES, instance=client)

		return self.render_to_response({
			'form': client_form,
			'formset': inline_formset,
			'client': client,
		})


class ClientFinancialView(TemplateView):
	template_name = "client/financial_department.html"


	def get(self, request, client_id=None):
		if client_id:
			client = Client.objects.get(pk=client_id)
		else:
			return redirect("client_home")

		inline_formset = ClientPaymentFormSet(instance=client)

		return self.render_to_response({
			"formset": inline_formset,
			"client": client,
		})


	def post(self, request, client_id=None):
		pass


class ClientFinancialListView(ListView):
	template_name = 'client/index.html'
	model = Client