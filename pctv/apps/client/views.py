# -*- coding: utf-8 -*-
# Create your views here.
from django.views.generic import TemplateView, ListView
from django.http import Http404
from django.shortcuts import redirect
from django.db.models import Q

from models import Client, CLIENT_STATUS
from forms import ClientPaymentFormSet, ClientForm, ClientPaymentCollectFormSet
from apps.utils import MONTHS_DICT, get_reverse_months_header
from apps.prospection.models import TOTAL_INCOME_BUCKET, Prospection
from apps.utils.views import JSONTemplateRenderMixin, CSVRenderMixin
import operator


class ClientView(CSVRenderMixin, ListView):
    model = Client
    template_name = 'client/index.html'
    queryset = Client.objects.exclude(status=u"Cancelado")
    csv_filename = "clientes.csv"

    def prepare_data(self, queryset):
        """ Really long string of data that needs be rendered """
        prepared_data = list()
        # Get a nicely ordered set of keys
        keys = [
            "id",
            "prospection__father_lastname",
            "prospection__mother_lastname",
            "prospection__first_name",
            "prospection__middle_name",
            "inventory__unique_id",
            "integration_date",
            "signature_date",
            "auth_date",
            "pricing_date",
            "payment_date",
            "notary",
            "delivery_date",
            "created_date",
            "status"
        ]
        
        values = queryset.values(*keys)

        prepared_data.append(keys)

        for v in values:
            row = list()
            for key in keys:
                if isinstance(v[key], unicode):
                    data = v[key].encode("utf8")
                else:
                    data = v[key]
                row.append(data)
            try:
                prepared_data.append(row)
            except UnicodeEncodeError:
                print "PROBLEM"
                continue
        return prepared_data

    def generate_file_download(self, data_list):
        """Overriding stuff on the CSV mixin"""
        return super(ClientView, self).generate_file_download(data_list)

    def get(self, request, *args, **kwargs):
        """Meh"""
        if request.GET.get("format", None):
            return self.render_csv_to_response(self.queryset)
        else:
            return super(ClientView, self).get(request, *args, **kwargs)

class ClientAjaxView(JSONTemplateRenderMixin, ListView):
    template_name = "client/partials/table.html"
    model = Client

    def get_queryset(self):
        """
        Depending on sent filters from request.GET return a relevant
        queryset. The parameters passed are month (NOVIEMBRE 2012),
        status and income bracket (De 13,000 a 20,000)

        Arguments:
        - `self`: Self reference. Pretty straight forward
        """
        month = self.request.GET.get("month", None)
        income = self.request.GET.get("income", None)
        status = self.request.GET.get("status", None)
        query = Q()

        if month:
            # Split it up and get year, month
            month, year = month.split(" ")
            month = MONTHS_DICT[month]
            query = query & Q(created_date__month=month, created_date__year=year)
        if status:
            # Now search for a relevant status
            query = query & Q(status=status)
        if income:
            # Convert to correct integer representation
            income_tuple = (x[0] for x in TOTAL_INCOME_BUCKET if x[1] == income)

            # Now a relevant income bracket
            query = query & Q(prospection__total_income=income_tuple.next())

        return self.model.objects.filter(query)


class ClientDashboardView(TemplateView):
    template_name = 'client/dashboard.html'

    def get(self, request):
        # Get every client that has a signature date of today 'till 4 months in the future
        months = get_reverse_months_header()
        
        # Check if the user is a Vendedor. If the user is a vendedor only
        # show this user the clients that belong to him
        if request.user.groups.filter(name="Ventas").count():
            clients = Client.objects.filter(prospection__salesperson__pk=request.user.pk)
        else:
            clients = Client.objects.all()
        

        object_dict = dict()
        for c in CLIENT_STATUS:
            object_dict[c[0]] = clients.filter(status=unicode(c[1]))

        object_dict = sorted(object_dict.iteritems(), key=operator.itemgetter(0))

        new_object_dict = dict()
        for c in TOTAL_INCOME_BUCKET:
            new_object_dict[c[1]] = clients.filter(prospection__total_income=c[0])

        new_object_dict = sorted(new_object_dict.iteritems(), key=operator.itemgetter(0))

        return self.render_to_response({
            "months": months,
            "object_dict": object_dict,
            "new_object_dict": new_object_dict
        })


class ClientEditView(TemplateView):
    template_name = 'client/new_form.html'

    def get(self, request, ct="client", resource_id=None):
        """
        Render the forms and whatnot
        """
        if resource_id:
            # There must be a simpler way... have no idea though
            if ct == "prospection":
                client = Client(prospection=Prospection.objects.get(pk=resource_id))
            else:
                client = Client.objects.get(pk=resource_id)
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

    def post(self, request, ct="client", resource_id=None):
        """
        Save the form and create relevant records
        """
        client = Client()

        if resource_id:
            if ct == "prospection":
                try:
                    client = Client.objects.get(prospection__pk=int(resource_id))
                except Client.DoesNotExist:
                    client = Client(prospection=Prospection.objects.get(pk=int(resource_id)))
            else:
                client = Client.objects.get(pk=int(resource_id))

        client_form = ClientForm(request.POST, request.FILES, instance=client)

        if client_form.is_valid():
            created_client = client_form.save()

            print created_client.pk

            created_client.prospection.status = u"Apartado"
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

        inline_formset = ClientPaymentCollectFormSet(instance=client)

        return self.render_to_response({
            "formset": inline_formset,
            "client": client,
        })

    # What broke this were the disabled fields. Apparently they don't play nice with django forms
    # TODO: Find a way to just display data since perhaps allowing editions of certain fields is not a good idea
    def post(self, request, client_id=None):
        client = Client()
        if client_id:
            client = Client.objects.get(pk=client_id)

        inline_formset = ClientPaymentCollectFormSet(request.POST, request.FILES, instance=client)
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


class ClientReturnToProspectionView(TemplateView):
    """
    Just change the status of the prospection, delete the client with everything pertaining
    and that's it
    """
    def get(self, request, client_id=None):
        """
        Change the status, delete client and redirect to prospection view
        Arguments:
        - `self`: Duh
        - `request`: The django HTTP request object
        """
        try:
            client = Client.objects.get(pk=client_id)
            client.inventory.construction_status = u"Libre"
            client.inventory.save()

            # Delete everything else
            client.prospection.delete()
            client.delete()
            return redirect("client_home")
        except Client.DoesNotExist:
            raise Http404
