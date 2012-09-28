# Create your views here.
from django.views.generic import TemplateView, ListView
from django.shortcuts import redirect

from models import Client, CLIENT_STATUS
from forms import ClientPaymentFormSet, ClientForm
from apps.utils import format_time_span, MONTHS
import datetime
import operator


class ClientView(ListView):
    template_name = 'client/index.html'
    model = Client


class ClientDashboardView(TemplateView):
    template_name = 'client/dashboard.html'

    def get(self, request):
        # Get every client that has a signature date of today 'till 4 months in the future
        today = datetime.date.today()
        months = list()
        for x in xrange(1, 5):
            then = today + datetime.timedelta(days=31 * x)
            months.append("1RA de " + MONTHS[then.month - 1])
            months.append("2DA de " + MONTHS[then.month - 1])

        object_dict = dict()
        for c in CLIENT_STATUS:
            object_dict[c[0]] = Client.objects.filter(status=unicode(c[1]))

        object_dict = sorted(object_dict.iteritems(), key=operator.itemgetter(0))

        return self.render_to_response({
            "months": months,
            "object_dict": object_dict,
        })


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
        client = Client()
        if client_id:
            client = Client.objects.get(pk=client_id)

        inline_formset = ClientPaymentFormSet(request.POST, request.FILES, instance=client)
        if inline_formset.is_valid():
            inline_formset.save()
            return redirect("client_home")

        return self.render_to_response({
            'formset': inline_formset,
            'client': client,
        })


class ClientFinancialListView(ListView):
    template_name = 'client/index.html'
    model = Client


class ClientSalesView(TemplateView):
    tempate_name = 'client/index.html'


class ClientDownpaymentView(TemplateView):
    template_name = 'client/index.html'
