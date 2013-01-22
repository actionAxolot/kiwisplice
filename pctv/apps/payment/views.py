# -*- coding: utf-8 -*-
# Create your views here.
from django.db.models import Q
from django.utils.datastructures import SortedDict
from django.views.generic import TemplateView, ListView
from apps.utils import get_months_header, MONTHS_DICT
from apps.client.models import Client
from apps.utils.views import JSONTemplateRenderMixin


class PaymentDashboard(TemplateView):
    template_name = "payment/dashboard.html"

    def get(self, request, *args, **kwargs):
        # Now generate the first dashboard datastructure
        months = get_months_header()

        # Get enganche by Unidad
        clients = Client.objects.all()

        # Now separate by it's needed parameters
        statuses = ("Actual", "Pagado", "Vencido")

        object_list = SortedDict()
        for s in statuses:
            object_list[s] = clients.filter(payment__status=s).distinct()

        ctx = {
            "months": months,
            "object_list": object_list
        }

        return self.render_to_response(ctx)


class PaymentAjaxView(JSONTemplateRenderMixin, ListView):
    template_name = "payment/partials/table.html"
    model = Client

    def get_queryset(self):
        date = self.request.GET.get("date", None)
        status = self.request.GET.get("status", None)
        query = Q()

        if date:
            month, year = date.split(" ")
            query = query & Q(payment__date_due__month=MONTHS_DICT[month], payment__date_due__year=year)

        if status:
            query = query & Q(payment__status=status)

        return self.model.objects.filter(query)


class PaymentView(TemplateView):
    template_name = 'payment/index.html'
