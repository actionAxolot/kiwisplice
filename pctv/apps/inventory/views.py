# Create your views here.
from django.views.generic import TemplateView, ListView
from django.shortcuts import redirect
from models import Inventory
from forms import InventoryForm

class InventoryView(ListView):
	template_name = "inventory/index.html"
	model = Inventory


class InventoryDeleteView(TemplateView):
	def get(self, request, inventory_id=None):
		if inventory_id:
			Inventory.objects.get(pk=inventory_id).delete()
			return redirect('inventory_home')


class InventoryCreateView(TemplateView):
	template_name = "inventory/new_form.html"

	def get(self, request, inventory_id=None):
		inventory = Inventory()
		if inventory_id:
			inventory = Inventory.objects.get(pk=inventory_id)

		inventory_form = InventoryForm(instance=inventory, user=request.user)

		return self.render_to_response({
			"form": inventory_form
		})


	def post(self, request, inventory_id=None):
		inventory = Inventory()
		if inventory_id:
			inventory = Inventory.objects.get(pk=inventory_id)
		inventory_form = InventoryForm(request.POST, request.FILES, instance=inventory, user=request.user)
		if inventory_form.is_valid():
			inventory_form.save()
			return redirect("inventory_home")

		return self.render_to_response({
			"form": inventory_form,
		})