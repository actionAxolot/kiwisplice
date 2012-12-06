# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import redirect
from django.utils.datastructures import SortedDict
from models import (Inventory, Section,
    Prototype, BridgeCredit, PERCENTAGES_OPTIONS, CONSTRUCTION_STATUS, BRIDGE_CREDIT_STATUSES)
from forms import (InventoryForm, SectionForm,
    PrototypeForm, BridgeCreditForm, BridgeCreditPaymentsFormset)
from django.db.models import Q
from apps.utils.views import JSONTemplateRenderMixin, JSONRenderMixin
from apps.utils import get_months_header, MONTHS_DICT
from django.db.models import Sum
from django import http
from django.utils import simplejson as json


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
        inventory_form = InventoryForm(request.POST, request.FILES, 
                                       instance=inventory, user=request.user)
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
    template_name = "inventory/bridge/bridge_credit_index.html"
    model = BridgeCredit


class InventoryBridgeCreditCreateView(TemplateView):
    template_name = "inventory/bridge/bridge_credit_new_form.html"

    def get(self, request, bridge_credit_id=None):
        bridge_credit = BridgeCredit()
        if bridge_credit_id:
            bridge_credit = BridgeCredit.objects.get(pk=bridge_credit_id)
        
        if request.GET.get("inventario", None):
            form = BridgeCreditForm(instance=bridge_credit, initial={"inventory": request.GET.get("inventario")})
        else:
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


class InventoryDeliveryOrderView(TemplateView):
    """
    Just generate fucking documents. Ugh...
    """
    template_name = "inventory/documents/orden_entrega.html"


# ------- START RETARDED MAP THING ---------
class InventoryCrappyMapView(TemplateView):
    """
    Fucking hate these maps that no-one will use
    """
    template_name = "inventory/map.html"
    available_colors = (
        "blue",
        "green", 
        "orange",
        "pink",
        "red",
        "white",
        "yellow",
    )

    def get(self, request, **kwargs):
        """
        Depending on filters return the correct queryset
        """
        return self.render_to_response({})


class InventoryAjaxCrappyMapView(JSONRenderMixin, ListView):
    template_name = None
    model = Inventory

    available_colors = (
        "blue",
        "green",
        "orange",
        "pink",
        "red",
        "white",
        "yellow",
    )

    def get_context_data(self, *args, **kwargs):
        context = dict()
        sel_filter = self.request.GET.get("filter", "construction_status")
        legend = dict()
        result = dict()
        if sel_filter == "construction_status": # By construction status
            i = 0
            for e in CONSTRUCTION_STATUS:
                legend[e[0]] = self.available_colors[i]
                i += 1

            result["data"] = dict()
            for inv in self.model.objects.all().values("construction_status"):
                result["data"][inv["construction_status"]] = list()
            for inv in self.model.objects.all().values("construction_status", "x", "y"):
                result["data"][inv["construction_status"]].append((float(inv.get("x", 0)), float(inv.get("y", 0))))

        if sel_filter == "bridgecredit_status": # By bridge credit status
            i = 0
            for e in BRIDGE_CREDIT_STATUSES:
                legend[e[0]] = self.available_colors[i]
                i += 1

            result["data"] = self.model.objects.values("bridgecredit__status", "x", "y")

        if sel_filter == "percent_complete": # By construction percentage
            # First get the retarded ranges
            temp = {"0": list(), "10-30": list(), "40-70": list(), "80-90": list(), "100": list()}
            for inv in self.model.objects.all():
                if inv.percent_completed == 0:
                    temp["0"].append(inv)
                if inv.percent_completed >= 10 and inv.percent_completed <= 30:
                    temp["10-30"].append(inv)
                if inv.percent_completed >= 40 and inv.percent_completed <= 70:
                    temp["40-70"].append(inv)
                if inv.percent_completed >= 80 and inv.percent_completed <= 90:
                    temp["80-90"].append(inv)
                if inv.percent_completed == 100:
                    temp["100"].append(inv)
            i = 0
            for k, v in temp.items():
                legend[k] = self.available_colors[i]
                i += 1
            result["data"] = temp

        if sel_filter == "client_status_in": # By client status
            allowed_statuses = ("Cancelado", "Firmado", "Viv. entregada", "Autorizado")
            result["data"] = self.model.objects.filter(client__status__in=allowed_statuses).values(sel_filter, "x", "y")

            i = 0
            for s in allowed_statuses:
                legend[s] = self.available_colors[i]
                i += 1

        context["legend"] = legend
        context["data"] = result
        return context


class InventoryDashboardView(TemplateView):
    template_name = "inventory/dashboard.html"

    def get(self, request, *args, **kwargs):
        """
        Create the appropiate datastructures
        to display in the different dashboard tables
        """
        sections = Section.objects.all().order_by("-name")
        d_section = dict() # Ordered by section, display total and how much $$ earned
        o_section = dict() # Order by section, display % of completion and when it'll be completed
        s_section = dict() # Order by status, display

        for s in sections:
            # How many prototypes?
            prototypes = Prototype.objects.filter(inventory__section=s).distinct()

            d_section[s.name] = {}
            for p in prototypes:
                d_section[s.name][p.name] = p.inventory_set.filter(prototype=p, section=s)
            
        for s in sections:
            o_section[s.name] = {}
            qs = s.inventory_set.all()
            blocks = set([x.block for x in qs])

            # Now that you have the necessary info
            for b in blocks:
                o_section[s.name][b] = {}
                for p in PERCENTAGES_OPTIONS:
                    temp = qs.filter(percent_completed=p[0], section=s, block=b)
                    if temp:
                        o_section[s.name][b][p[0]] = temp
                    else:
                        continue

        # Create necessary headers
        special_headers = [x[0] for x in CONSTRUCTION_STATUS]
        for s in sections:
            s_section[s.name] = {}
            prototypes = Prototype.objects.filter(inventory__section=s)
            for p in prototypes:
                s_section[s.name][p.name] = s.inventory_set.filter(prototype=p)

        return self.render_to_response({
                "d_section": d_section,
                "o_section": o_section,
                "s_section": s_section,
                "months": get_months_header,
                "special_headers": special_headers,
        })


class InventoryAjaxView(JSONTemplateRenderMixin, ListView):
    template_name = "inventory/partials/table.html"
    model = Inventory


    def get_queryset(self):
        section = self.request.GET.get("section", None)
        prototype = self.request.GET.get("prototype", None)
        block = self.request.GET.get("block", None)
        date_source_const = self.request.GET.get("date-const", None)
        status = self.request.GET.get("status", None)

        query = Q()

        if section:
            query = query & Q(section__name__iexact=section)
        if prototype:
            query = query & Q(prototype__name__iexact=prototype)
        if block:
            block = block if len(block) > 1 else "0%s" %(block)
            query = query & Q(block=block)
        if date_source_const:
            # Prepare to a readable format
            month, year = date_source_const.split(" ")
            month = MONTHS_DICT[month]
            query = query & Q(construction_end_date__month=month, construction_end_date__year=year)
        if status:
            query = query & Q(construction_status=status)

        return self.model.objects.filter(query)


class InventoryBridgeCreditDashboard(TemplateView):
    template_name = "inventory/bridge/dashboard.html"

    def get(self, request, *args, **kwargs):
        # Build the specialized datastructures you need for those stupid dashboards
        special_headers = [x[0] for x in BRIDGE_CREDIT_STATUSES]
        special_headers.append("TOTAL")

        bridges = BridgeCredit.objects.all()
        n_credit = dict()
        t_credit = dict()

        for c in CONSTRUCTION_STATUS:
            qs = bridges.filter(inventory__construction_status=c[0])
            tmp = SortedDict()
            n_credit[c[0]] = None
            for s in special_headers:
                if s == "TOTAL":
                    tmp[s] = len(qs)
                else:
                    tmp[s] = len(qs.filter(status=s))
            n_credit[c[0]] = tmp

        for c in CONSTRUCTION_STATUS:
            qs = bridges.filter(inventory__construction_status=c[0])
            tmp = SortedDict()
            t_credit[c[0]] = None
            for s in special_headers:
                if s == "TOTAL":
                    kewlness = qs.aggregate(total=Sum("bridgecreditpayment__amount"))["total"]
                    if kewlness:
                        tmp[s] = kewlness
                    else:
                        tmp[s] = 0.00
                else:
                    kewlness = qs.filter(status=s).aggregate(total=Sum("bridgecreditpayment__amount"))["total"]
                    if kewlness:
                        tmp[s] = kewlness
                    else:
                        tmp[s] = 0.00
            t_credit[c[0]] = tmp

        return self.render_to_response({"n_credit": n_credit, "t_credit": t_credit,
                                        "special_headers": special_headers})


class InventoryBridgeCreditAjax(JSONTemplateRenderMixin, ListView):
    template_name = "inventory/bridge/partials/table.html"
    model = BridgeCredit

    def get_queryset(self, *args, **kwargs):
        const_status = self.request.GET.get("const-status", None)
        bridge_status = self.request.GET.get("bridge-status", None)
        if bridge_status == "TOTAL":
            bridge_status = None
        query = Q()

        if const_status:
            query = query & Q(inventory__construction_status=const_status)
        if bridge_status:
            query = query & Q(status=bridge_status)

        return self.model.objects.filter(query)
