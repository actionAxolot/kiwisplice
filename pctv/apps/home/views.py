# Create your views here.
from django.views.generic import TemplateView, RedirectView, ListView
from django.core.urlresolvers import reverse
from django.utils.datastructures import SortedDict
from django.http import Http404
from django.db.models import Q
from apps.client.models import Client
from apps.utils import get_months_header, MONTHS_DICT
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
        Render the necessary table and shit. Pretty nice huh?
        """
        context = super(ListView, self).get_context_data(*args, **kwargs)
        # Now arrange everything neatly in rows
        context["months"] = get_months_header()
        clientes = SortedDict()
        clientes["Apartado"] = Client.objects.filter(prospection__status="Apartado")
        clientes["Por Firmar"] = Client.objects.filter(status="Por firmar")
        clientes["Firmado"] = Client.objects.filter(status="Firmado")
        clientes["Viv. Entregada"] = Client.objects.filter(status="Viv. Entregada")
        clientes["Cancelado"] = Client.objects.filter(status="Cancelado")
        context["object_list"] = clientes
        
        return context
    

class HomeAjaxView(JSONTemplateRenderMixin, ListView):
    """
    Render a table as a template and display it in a popup
    """
    template_name = "client/partials/table.html"
    model = Client

    def get_queryset(self, *args, **kwargs):
        """
        Pretty much like the one in apps.client.views
        """
        month = self.request.GET.get("month", None)
        status = self.request.GET.get("status", None)
        query = Q()
        # Split and get year and month
        if month:
            month, year = month.split(" ")
            month = MONTHS_DICT[month]
            query = query & Q(created_date__month=month, created_date__year=year)
        if status:
            if status == "Apartado":
                query = query & Q(prospection__status=status)
            else:
                query = query & Q(prospection__status=status)

        return self.model.objects.filter(query)
