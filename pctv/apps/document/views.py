from django.views.generic import TemplateView, RedirectView
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.db.models import Sum
from apps.prospection.models import Prospection
from apps.client.models import Client
from apps.inventory.models import Inventory
import datetime
from decimal import Decimal

class DocsView(TemplateView):
    """
    Just a small placeholder view shit thing to create the HTML documents necessary.
    """

    available_templates = {
        "entrega": "document/entrega.html",
        "escrituracion": "document/escrituracion.html",
        "ubicacion": "document/ubicacion.html",
        "contrato": "document/contrato.html",
    }

    def get(self, request):
        """
        According to the passed GET paramenter 'op' render the required template
        and pk as the prospection ID to laod. Also there'll need
        to be some data... but I can't think of how to accomodate that yet
        Arguments:
        - `self`: Object reference
        - `request`: Request object passed by django
        """
        op = request.GET.get("op", None)
        if op == "entrega" or op == "escrituracion":
            context = self.render_entrega_escrituracion(request.GET.get("pk", 1), op)
        elif op == "ubicacion":
            context = self.render_ubicacion(request.GET.get("pk", 1), request.GET.get("new-pk", 2))
        else:
            context = self.render_contrato(request.GET.get("pk", 1))

        return self.render_to_response(context)

    def render_entrega_escrituracion(self, prospection_id, reason="entrega"):
        try:
            prospection = Prospection.objects.get(pk=prospection_id)
        except Prospection.DoesNotExist:
            raise Http404

        # Get credits total and shit
        credit_info = dict()
        credit_info["total"] = prospection.client_set.all()[0].payment_set.all().aggregate(total=Sum("amount"))
        credit_info["payed"] = prospection.client_set.all()[0].payment_set.all().filter(status="Pagado").aggregate(total=Sum("amount"))

        # We should kind of safeguard this here because I have no clue on how this will work.
        # If 0 just.. probably... render with 0's and shit
        if not credit_info["total"]["total"]:
            credit_info["total"]["total"] = 0

        if not credit_info["payed"]["total"]:
            credit_info["payed"]["total"] = 0

        credit_info["difference"] = credit_info["total"]["total"] - credit_info["payed"]["total"]
        self.template_name = self.available_templates.get(reason)
        return {"p": prospection, "credit": credit_info}

    def render_ubicacion(self, client_id, new_location_id):
        try:
            client = Client.objects.get(pk=client_id)
            new_location = Inventory.objects.get(pk=new_location_id)
        except (Client.DoesNotExist, Inventory.DoesNotExist):
            raise Http404

        self.template_name = self.available_templates.get("ubicacion")
        return {"client": client, "new_location": new_location}


    def render_contrato(self, client_id):
        try:
            client = Client.objects.get(pk=client_id)
            total_payed = client.payment_set.filter(status="Pagado").aggregate(total=Sum("amount"))["total"]
            try:
                total_left = client.inventory.get_price() - total_payed
            except TypeError:
                total_left = client.inventory.get_price()
                total_payed = Decimal("0.00")
            expiry_date = client.inventory.construction_end_date + datetime.timedelta(days=30)
        except Client.DoesNotExist:
            raise Http404
        self.template_name = self.available_templates.get("contrato")
        return {
            "client": client,
            "total_payed": total_payed,
            "total_left": total_left,
            "expiry_date": expiry_date,
            "today_date": datetime.date.today()
        }

