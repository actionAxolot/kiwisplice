# Create your views here.
from django.views.generic import TemplateView, ListView
from django.shortcuts import redirect
from models import (Inventory, Section,
    Prototype, BridgeCredit)
from forms import (InventoryForm, SectionForm,
    PrototypeForm, BridgeCreditForm, BridgeCreditPaymentsFormset)


# <----- START LANDING PAGE ------>
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
            "form": inventory_form,
            'inventory': inventory,
            'inventory_id': inventory_id,
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
            'inventory': inventory,
            'inventory_id': inventory_id,
        })


# <----- START PROTOTYPE ------>
class InventoryPrototypeView(ListView):
    template_name = "inventory/prototype_index.html"
    model = Prototype


class InventoryPrototypeCreateView(TemplateView):
    template_name = "inventory/prototype_new_form.html"

    def get(self, request, prototype_id=None):
        prototype = Prototype()
        if prototype_id:
            prototype = Prototype.objects.get(pk=prototype_id)

        form = PrototypeForm(instance=prototype)

        return self.render_to_response({
            "form": form,
        })

    def post(self, request, prototype_id=None):
        prototype = Prototype()
        if prototype_id:
            prototype = Prototype.objects.get(pk=prototype_id)

        form = PrototypeForm(request.POST, request.FILES, instance=prototype)

        if form.is_valid():
            form.save()
            return redirect("inventory_prototype")

        return self.render_to_response({
            "form": form,
        })


class InventoryPrototypeDeleteView(TemplateView):
    def get(self, request, prototype_id=None):
        Prototype.objects.get(pk=prototype_id).delete()



# <----- START SECTION ------>
class InventorySectionView(ListView):
    template_name = "inventory/section_index.html"
    model = Section


class InventorySectionCreateView(TemplateView):
    template_name = "inventory/section_new_form.html"

    def get(self, request, section_id=None):
        section = Section()
        if section_id:
            section = Section.objects.get(pk=section_id)

        form = SectionForm(instance=section)

        return self.render_to_response({
            'form': form,
        })

    def post(self, request, section_id=None):
        section = Section()
        if section_id:
            section = Section.objects.get(pk=section_id)

        form = SectionForm(request.POST, request.FILES, instance=section)

        if form.is_valid():
            form.save()
            return redirect("inventory_section")
        else:
            return self.render_to_response({
                "form": form,
            })


class InventorySectionDeleteView(TemplateView):
    def get(self, request, section_id=None):
        Section.objects.get(pk=section_id).delete()
        return redirect("inventory_section")


# <----- Bridge Credit ----->
class InventoryBridgeCreditView(ListView):
    template_name = "inventory/bridge_credit_index.html"
    model = BridgeCredit


class InventoryBridgeCreditCreateView(TemplateView):
    template_name = "inventory/bridge_credit_new_form.html"

    def get(self, request, bridge_credit_id=None):
        bridge_credit = BridgeCredit()
        if bridge_credit_id:
            bridge_credit = BridgeCredit.objects.get(pk=bridge_credit_id)

        form = BridgeCreditForm(instance=bridge_credit)
        inline_formset = BridgeCreditPaymentsFormset(instance=bridge_credit)

        return self.render_to_response({
            'form': form,
            'inline_formset': inline_formset,
        })

    def post(self, request, bridge_credit_id=None):
        bridge_credit = BridgeCredit()
        if bridge_credit_id:
            bridge_credit = BridgeCredit.objects.get(pk=bridge_credit_id)

        form = BridgeCreditForm(request.POST, request.FILES, instance=bridge_credit)
        if form.is_valid():
            created_credit = form.save()
            inline_formset = BridgeCreditPaymentsFormset(request.POST, request.FILES, instance=created_credit)
            if inline_formset.is_valid():
                inline_formset.save()
                if request.POST.get("add-another", None):
                    return redirect("inventory_bridge_credit_create_params", bridge_credit_id=created_credit.pk)
                else:
                    return redirect("inventory_bridge_credit")

        return self.render_to_response({
            "form": form,
            "inline_formset": inline_formset,
        })


class InventoryBridgeCreditDeleteView(TemplateView):
    def get(self, request, bridge_credit_id):
        BridgeCredit.objects.get(pk=bridge_credit_id).delete()
        return redirect("inventory_bridge_credit")
