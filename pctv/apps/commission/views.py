# Create your views here.
from django.views.generic import TemplateView, ListView
from django.contrib.auth.models import User
from django.db.models import F, Count
from django.contrib.contenttypes.models import ContentType
from models import Commission, CommissionPayment
from apps.client.models import Client
from apps.inventory.models import Inventory


class CommissionDashboardView(TemplateView):
    template_name = 'commission/index.html'
    def get(self, request):
        # Get all salespeople that have clients... ergo commissions
        # TODO: Refactor this to use Q objects and such to form dynamic queries
        if request.user.is_superuser:
            salespeople = User.objects.annotate(Count("prospection__client")) \
                .filter(prospection__client__count__gt=0).distinct().order_by("-id")
    
            # Clients
            clients = Client.objects.all().order_by("-id")
    
            # Inventory
            inventory = Inventory.objects.filter(construction_status="Con cliente").order_by("-id")
        else:
            salespeople = User.objects.annotate(Count("prospection__client")).filter(prospection__client__count__gt=0) \
                .filter(pk=request.user.pk)
                
            clients = Client.objects.filter(prospection__salesperson=request.user).order_by("-id")
            
            inventory = Inventory.objects.filter(client__prospection__salesperson=request.user,
                                                  construction_status="Con cliente").order_by("-id")
        
        return self.render_to_response(
            {
                "clients": clients,
                "salespeople": salespeople,
                "inventory": inventory,
            }
        )

class CommissionPaymentView(ListView):
    template_name = "commission/payment_view.html"

    def get_queryset(self):
        return CommissionPayment.objects.filter(commission__pk=self.args[0])
    

class CommissionAjaxView(TemplateView):
    """ Just return a rendered table template with the relevant commission data """
    template_name = 'commission/ajax_template.html'

    def get(self, request):
        # How the fuck do you render a template?
        model = request.GET.get("model", "user")
        app_label = request.GET.get("app_label", "auth")
        model_id = request.GET.get("id", "1")

        # This is upside-down
        is_tabbed = request.GET.get("is_tabbed", False)

        # Now get the pertaning model and it's objects
        object_model = ContentType.objects.get(app_label=app_label, model=model).get_object_for_this_type(pk=model_id)
        if app_label == "auth":
            commissions = Commission.objects.filter(client__prospection__salesperson=object_model)
        elif app_label == "client":
            commission_payments = CommissionPayment.objects.filter(commission__client=object_model)
        elif app_label == "inventory":
            commission_payments = CommissionPayment.objects.filter(commission__client__inventory=object_model)

        if is_tabbed == "false":
            ctx = {"commission_payments": commission_payments}
            self.template_name = "commission/ajax_payment_template.html"
            return self.render_to_response(ctx)
        else:
            ctx = {
                "pending": commissions.filter(status="Pendiente"),
                "payed": commissions.filter(status="Pagado"),
                "canceled": commissions.filter(status="Cancelado"),
            }

        return self.render_to_response(ctx)

