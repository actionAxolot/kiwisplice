# -*- coding: utf-8 -*-
# Create your views here.
from django.views.generic import TemplateView, ListView
from apps.utils import get_months_header


# Create your views here.
class PaymentDashboard(TemplateView):
    template_name = "payment/dashboard.html"

    def get(self, request, *args, **kwargs):
        # Generate the month headers
        months = get_months_header()

        # Now generate the first dashboard datastructure
        
        
        ctx = {
            "months": months
        }

        return self.render_to_response(ctx)


class PaymentView(TemplateView):
    template_name = 'payment/index.html'

