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
        clients_by_status = clients.filter(payment__status="Actual").exclude(payment__status__in=("Pagado", "Vencido")).distinct()

        # Now get the totals
        total_pagados = clients.filter(payment__status="Pagado").distinct()
        total_vencido = clients.filter(payment__status="Vencido").distinct()

        print "total_pagados %d" % len(total_pagados)
        print "total_vencido %d" % len(total_vencido)

        object_list = SortedDict()
        object_list["Actual"] = clients_by_status

        ctx = {
            "months": months,
            "object_list": object_list,
            "total_pagados": total_pagados,
            "total_vencido": total_vencido,
        }

        return self.render_to_response(ctx)


class PaymentAjaxView(JSONTemplateRenderMixin, ListView):
    template_name = "payment/partials/table.html"
    model = Client

    def split_date_tokens(self, date_string):
        """ TODO: Same fucking implementation that can be seen everywhere. What was wrong with me! """
        month, year = date_string.split(" ")
        month = MONTHS_DICT[month]
        return month, year

    def get_date_query(self, date_list, query=Q()):
        """ TODO: Totally proud of this... although it also has a quintillion implementations in the code
         If python had tail call optimizations this would fly"""
        if len(date_list):
            month, year = self.split_date_tokens(date_list.pop())
            query = query | Q(payment__date_due__month=month, payment__date_due__year=year)
            return self.get_date_query(date_list, query=query)
        return query

    def get_queryset(self):
        date = self.request.GET.get("date", None)
        status = self.request.GET.get("status", None)
        query = Q()

        if date and date != "NONE":
            month, year = date.split(" ")
            query = query & Q(payment__date_due__month=MONTHS_DICT[month], payment__date_due__year=year)

        if status:
            if not date and date != "NONE":
                months_to_check = get_months_header()
                query = query & self.get_date_query(months_to_check)
            query = query & Q(payment__status=status)
        return self.model.objects.filter(query).distinct()


class PaymentView(TemplateView):
    template_name = 'payment/index.html'
