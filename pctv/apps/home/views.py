# Create your views here.
from django.views.generic import TemplateView, RedirectView, ListView
from django.core.urlresolvers import reverse
from django.utils.datastructures import SortedDict
from django.http import Http404
from django.db.models import Q
from apps.client.models import Client
from apps.prospection.models import Prospection
from apps.utils import get_reverse_months_header, get_months_header, MONTHS_DICT
from apps.utils.views import JSONTemplateRenderMixin


class HomeView(RedirectView):
    """
    Redirect accordingly. If user's not logged in redirect to login view
    else redirect to... prospections for now
    """
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            self.url = reverse("home_dashboard")
        else:
            self.url = reverse("login")

        return super(HomeView, self).get(self, request, *args, **kwargs)


class LoginView(TemplateView):
    """Display a login form and process credentials"""
    template_name = "home/index.html"


class DashboardView(ListView):
    """
    Dashboard showing latest client information
    """
    template_name = "home/dashboard.html"
    model = Client

    def get_context_data(self, *args, **kwargs):
        """
        Render a table with two rows, one containing prospections and one containing new clients
        """
        context = super(ListView, self).get_context_data(*args, **kwargs)
        # Now arrange everything neatly in rows
        context["months"] = get_reverse_months_header()
        clientes = SortedDict()
        clientes["prospecciones"] = Prospection.objects.all().exclude(client__isnull=False)
        clientes["clientes"] = Client.objects.all().exclude(status="Firmado")

        context["object_list"] = clientes
        return context


class HomeAjaxView(JSONTemplateRenderMixin, ListView):
    """
    Render a table as a template and display it in a popup
    IF no date is passed in the request, calculate the months and
    year of the past 9 months
    """
    template_name = "client/partials/table.html"
    model = Client

    def split_date_tokens(self, date_string):
        """Split the systems date tokens into something nicer to handle in Django"""
        # TODO: This is repeated a trillion times throught the code. Find a place to put it
        # and call it done. This is not nice in case something needs updating
        month, year = date_string.split(" ")
        month = MONTHS_DICT[month]
        return month, year

    def get_date_query(self, date_list, query=Q(), resource_type="prospection"):
        """date_dict is a set of dates formatted according to program specs.
        Return a Q object with a correct range of dates according to it"""
        # Is recursion really it?
        if len(date_list):
            month, year = self.split_date_tokens(date_list.pop())
            if resource_type == "prospection":
                query = query | Q(visitation_date__month=month, visitation_date__year=year)
            else:
                query = query | Q(created_date__month=month, created_date__year=year)
            return self.get_date_query(date_list, query=query, resource_type=resource_type)
        return query

    def get_queryset(self, *args, **kwargs):
        """
        Pretty much like the one in apps.client.views
        """
        date = self.request.GET.get("month", None)
        resource_type = self.request.GET.get("type", None)

        query = Q()

        # Split and get year and month
        if date:
            month, year = self.split_date_tokens(date)
            if resource_type == "prospection":
                query = query & Q(visitation_date__month=month, visitation_date__year=year)
            else:
                query = query & Q(created_date__month=month, created_date__year=year)
        else:
            months_to_check = get_reverse_months_header()
            query = query & self.get_date_query(months_to_check, resource_type=resource_type)
            
        # This is a bit patchy 
        # TODO: Fix it up a little. Perhaps break it up into another function?
        if resource_type == "prospection":
            self.template_name = "prospection/ajax/prospection_detail_table.html"
            return Prospection.objects.filter(query)
        else:
            return self.model.objects.filter(query)
