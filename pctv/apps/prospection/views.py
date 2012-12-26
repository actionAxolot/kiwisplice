# -*- coding: utf-8 -*-
# Create your views here.
from apps.client.models import Client
from apps.prospection.forms import FilterForm
from django import http
from django.shortcuts import redirect
from django.template import Context, loader
from django.utils import simplejson
from django.views.generic import ListView, TemplateView
from django.views.decorators.csrf import csrf_exempt
from forms import ProspectionForm, ProspectionPhoneNumberFormset
from models import Prospection, PROSPECTION_STATUS_CHOICES, \
    PROSPECTION_CHANNEL_OPTIONS, TOTAL_INCOME_BUCKET
import datetime
import operator
from django.http import Http404, HttpResponseRedirect
from apps.utils.views import JSONTemplate


class ProspectionView(ListView):
    model = Prospection
    queryset = Prospection.objects.all().exclude(status__in=("Apartado",))
    template_name = "prospection/index.html"


class ProspectionDashboardView(TemplateView):
    """Show the dashboard with kewl information for prospections"""
    template_name = "prospection/dashboard.html"

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(ProspectionDashboardView, self).dispatch(*args, **kwargs)

    def get(self, request):
        # Get the respective buckets
        obj_list = {}
        obj_pros_list = {}
        obj_status_list = {}

        for x in xrange(0, 10):
            obj_list[x] = Prospection.objects.get_by_weeks_old(weeks_old=x)

        obj_list = sorted(obj_list.iteritems(), key=operator.itemgetter(0))

        # Get totals and crap
        total_list = {}
        for p in PROSPECTION_STATUS_CHOICES:
            total_list[p[0]] = len(Prospection.objects.filter(status=p[0]))

        total_list["total_general"] = len(Prospection.objects.all())

        # Now work with the prospection channel table
        total_pros_list = {}
        for x in PROSPECTION_CHANNEL_OPTIONS:
            obj_pros_list[unicode(x[1])] = Prospection.objects.filter(prospection_channel=unicode(x[1]))

        for x in TOTAL_INCOME_BUCKET:
            total_pros_list[x[0]] = len(Prospection.objects.filter(total_income=int(x[0])))

        obj_pros_list = sorted(obj_pros_list.iteritems(), key=operator.itemgetter(0))

        total_status_list = {}
        for x in PROSPECTION_STATUS_CHOICES:
            obj_status_list[x[0]] = Prospection.objects.filter(status=x[0])

        for x in TOTAL_INCOME_BUCKET:
            total_status_list[x[0]] = len(Prospection.objects.filter(total_income=x[0]))

        obj_status_list = sorted(obj_status_list.iteritems(), key=operator.itemgetter(0))
        
        # Now get the prospections that have been caught this month
        month = datetime.date.today().month
        year = datetime.date.today().year
        obj_this_month = Prospection.objects.filter(visitation_date__month=month,
                                                    visitation_date__year=year)
        
        # Now create the new form
        time_filters = FilterForm()

        return self.render_to_response({
            'obj_list': obj_list,
            'total_list': total_list,
            'obj_pros_list': obj_pros_list,
            'total_pros_list': total_pros_list,
            'obj_status_list': obj_status_list,
            'obj_this_month': obj_this_month,
            'total_status_list': total_status_list,
            'time_filters': time_filters,
        })
        
    def post(self, request):
        # Ugh.. just do it here
        month = request.POST.get("month", datetime.date.today().month)
        year = request.POST.get("year", datetime.date.today().year)
        
        self.template_name = "prospection/ajax/time_filter.html"
        obj_this_month = Prospection.objects.filter(visitation_date__month=month,
                                                    visitation_date__year=year)
        
        return self.render_to_response({"obj_this_month": obj_this_month})


class ProspectionCreateView(TemplateView):
    template_name = "prospection/new_form.html"

    def post(self, request, prospection_id=None):
        prospection = Prospection()
        if prospection_id:
            prospection = Prospection.objects.get(pk=prospection_id)

        prospection_form = ProspectionForm(request.POST, request.FILES, instance=prospection)
        inline_formset = ProspectionPhoneNumberFormset(request.POST, instance=prospection)

        if prospection_form.is_valid():
            created_prospection = prospection_form.save()
            if created_prospection.status in ("Apartado",):
                try:
                    client = Client.objects.get(prospection=created_prospection)
                    if client.status == u"Cancelado":
                        client.status = u"Integración"
                        client.save()
                except Client.DoesNotExist:
                    client = Client(prospection=prospection)
                    client.save()

            inline_formset = ProspectionPhoneNumberFormset(request.POST,
                                                             instance=created_prospection)

            if inline_formset.is_valid():
                inline_formset.save()

                if created_prospection.status in ("Apartado",):
                    return redirect("client_edit", client_id=created_prospection.client_set.all()[0].pk)

                return redirect("prospection_home")

        return self.render_to_response({
            "form": prospection_form,
            "formset": inline_formset
        })

    def get(self, request, prospection_id=None):
        # Because even Apartado prospections need to be display in the
        # home report, they'll need to have a link for it. kind of
        # kewl but it makes for horrible design. If the Status is
        # Apartado redirect to the client create view
        if prospection_id:
            prospection = Prospection.objects.get(pk=prospection_id)
            prospection_form = ProspectionForm(instance=prospection)
        else:
            prospection = Prospection()
            prospection_form = ProspectionForm()

        inline_formset = ProspectionPhoneNumberFormset(instance=prospection)
        return self.render_to_response({
            "form": prospection_form,
            "formset": inline_formset,
        })


class ProspectionDeleteView(TemplateView):
    def get(self, request, prospection_id=None):
        Prospection.objects.get(pk=prospection_id).delete()
        return redirect("prospection_home")
    
    
class ProspectionByMonthView(TemplateView):
    template_name = "prospection/view_by_month.html"
    def get(self, request):
        month = request.GET.get("month", "1")
        year = request.GET.get("year", datetime.date.today().year)
        prospections = Prospection.objects.filter(visitation_date__month=month, visitation_date__year=year)
        
        return self.render_to_response({"prospections": prospections})
        


class ProspectionAjaxView(TemplateView):
    def get(self, request):
        # Get items out of the requestn
        date = request.GET.get("date", None)
        status = request.GET.get("status", None)
        # Get the correct objects
        prospections = list()
        if status and date:
            tmp_prospections = Prospection.objects.get_by_weeks_old(weeks_old=int(date))
            prospections = list()

            for p in tmp_prospections:
                if p.status == status:
                    prospections.append(p)
        elif status:
            prospections = Prospection.objects.filter(status=status)
        elif date:
            prospections = Prospection.objects.get_by_weeks_old(weeks_old=int(date))
        else:
            prospections = Prospection.objects.all()

        # Check for permissions here. For some reason they're not passed to the template
        can_delete = request.user.has_perm("prospection.delete_prospection")
        can_change = request.user.has_perm("prospection.change_prospection")

        return self.render_to_response({"object_list": prospections, "can_delete": can_delete, "can_change": can_change})

    def render_to_response(self, context):
        # Render the template
        t = loader.get_template("prospection/ajax/prospection_detail_table.html")
        data = {}
        data["template"] = t.render(Context(context))
        data["message"] = "success"
        return http.HttpResponse(simplejson.dumps(data, ensure_ascii=False), content_type="application/json")


class ProspectionAjaxChannelView(TemplateView):
    def get(self, request):
        income = request.GET.get("income", None)
        channel = request.GET.get("channel", None)

        prospections = list()
        if income and channel:
            prospections = Prospection.objects.filter(total_income=int(income), prospection_channel=channel)
        elif income:
            prospections = Prospection.objects.filter(total_income=int(income))
        elif channel:
            prospections = Prospection.objects.filter(prospection_channel=channel)
        else:
            prospections = Prospection.objects.all()

        return self.render_to_response({"object_list": prospections})

    def render_to_response(self, context):
        t = loader.get_template("prospection/ajax/prospection_detail_table.html")
        data = {}
        data["template"] = t.render(Context(context))
        data["message"] = "success"
        return http.HttpResponse(simplejson.dumps(data, ensure_ascii=False), content_type="application/json")


class ProspectionAjaxStatusView(TemplateView):
    def get(self, request):
        income = request.GET.get("income", None)
        status = request.GET.get("channel", None)

        if income and status:
            prospections = Prospection.objects.filter(total_income=int(income), status=status)
        elif income:
            prospections = Prospection.objects.filter(total_income=int(income))
        elif status:
            prospections = Prospection.objects.filter(status=status)
        else:
            prospections = Prospection.objects.all()

        return self.render_to_response({"object_list": prospections})

    def render_to_response(self, context):
        t = loader.get_template("prospection/ajax/prospection_detail_table.html")
        data = {}
        data["template"] = t.render(Context(context))
        data["message"] = "success"
        return http.HttpResponse(simplejson.dumps(data, ensure_ascii=False), content_type="application/json")


class ProspectionApartarView(TemplateView):
    """
    Change the status of a prospection to apartado after the
    click of a button
    """
    def get(self, request):
        """
        Receive in the request as a GET parameter the
        prospections ID and change the status. Then
        make the appropiate client changes and stuff
        """
        try:
            prospection = Prospection.objects.get(pk=request.GET.get("prospection_id"))
        except:
            raise Http404
        
        # Change the status to a more relevant 
        prospection.status = u"Apartado" # LOL This is super retarded
        prospection.save()
        if prospection.status in ("Apartado",):
            try:
                client = Client.objects.get(prospection=prospection)
                if client.status == u"Cancelado":
                    client.status = u"Integración"
                    client.save()
            except Client.DoesNotExist:
                client = Client(prospection=prospection)
                client.save()
        
        if request.user.has_perm("client.create_client"):
            return HttpResponseRedirect("/clientes-linea-de-produccion/editar/%d/" % client.pk)
        else:
            return HttpResponseRedirect("/prospeccion/ver/")