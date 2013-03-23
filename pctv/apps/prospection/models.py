# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes import generic
from apps.comment.models import Comment
from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _

import datetime


def get_week_range(date_in_week=None, number_of_weeks=None):
    # find out when week starts
    minus_one = datetime.timedelta(days=1)
    for x in xrange(date_in_week.weekday()):
        date_in_week = date_in_week - minus_one
    this_week_starts = date_in_week

    # Get N weeks ago date
    that_week_starts = this_week_starts - datetime.timedelta(days=7 * number_of_weeks)
    that_week_ends = that_week_starts + datetime.timedelta(days=6)

    return that_week_starts, that_week_ends


PROSPECTION_STATUS_CHOICES = (
    (u"Apartado", _(u"Apartado")),
    (u"No perfilado", _(u"No perfilado")),
    (u"Por cerrar", _(u"Por cerrar")),
    (u"Sin interés", _(u"Sin interés")),
    (u"Cancelado", _(u"Cancelado")),
)


PROSPECTION_FINANCIAL_OPTIONS = (
    (u"IMSS", _(u"IMSS")),
    (u"FOVISSSTE", _(u"FOVISSSTE")),
    (u"IPJAL", _(u"IPJAL")),
    (u"No cotiza", _(u"No Cotiza")),
)

TOTAL_INCOME_BUCKET = (
    (1, u"Hasta 12 Mil"),
    
    (2, u"Entre 12 y 18 Mil"),
    (3, u"Entre 18 y 25 Mil"),
    (4, u"Entre 25 y 35 Mil"),
    (5, u"Entre 35 y 45 Mil"),
    (6, u"Mayor a 45Mil"),
)


# Unecessary to separate.
PROSPECTION_CHANNEL_OPTIONS = (
    (u"Activación", _(u"Activación")),
    (u"Recomendado", _(u"Recomendado")),
    (u"Base de datos", _(u"Base de datos")),
    (u"Periódico", _(u"Periodico")),
    (u"Empresa", _(u"Empresa")),
    (u"Volanteo", _(u"Volanteo")),
    (u"Internet", _(u"Internet")),
    (u"Expo", _(u"Expo")),
    (u"Fraccionamiento", _(u"Fraccionamiento")),
    (u"Vendedor", _(u"Vendedor")),
    (u"Otro", _(u"Otro")),
)


class ProspectionManager(models.Manager):
    def get_by_weeks_old(self, weeks_old=None):
        if weeks_old < 9:
            init_date, end_date = get_week_range(datetime.date.today(), weeks_old)
            return self.get_query_set().filter(visitation_date__gte=init_date, visitation_date__lte=end_date)
        else:
            # TODO Date bug waiting to happen
            two_months_ago = datetime.date.today() - datetime.timedelta(days=56)

            return self.get_query_set().filter(visitation_date__lte=two_months_ago)


class Prospection(models.Model):
    salesperson = models.ForeignKey(User, blank=False, null=False,
        verbose_name=_(u'Vendedor'))
    financial_channel = models.CharField(blank=False, null=False,
        verbose_name=_(u"Canal Financiero"), max_length=50,
        choices=PROSPECTION_FINANCIAL_OPTIONS, default="IMSS")
    prospection_channel = models.CharField(blank=False, null=False,
        verbose_name=_(u"Canal Prospección"), max_length=50,
        choices=PROSPECTION_CHANNEL_OPTIONS, default="Fraccionamiento")
    visitation_date = models.DateField(blank=False, null=False, verbose_name=_(u"Fecha de visita"))
    status = models.CharField(blank=True, null=True, max_length=50,
        verbose_name=_(u"Status"), choices=PROSPECTION_STATUS_CHOICES, default="No perfilado")

    # Things to know... just in case...
    first_name = models.CharField(blank=False, null=False,
        max_length=50, verbose_name=_(u"Primer nombre"))
    middle_name = models.CharField(blank=True, null=True, max_length=50, verbose_name=_(u"Segundo nombre"))
    father_lastname = models.CharField(blank=False, null=False, max_length=50, verbose_name=_(u"Apellido Paterno"))
    mother_lastname = models.CharField(blank=True, null=True, max_length=50, verbose_name=_(u"Apellido Materno"))
    email = models.CharField(blank=False, null=False, max_length=50, verbose_name=_(u"Email"))

    street = models.CharField(null=True, max_length=50, verbose_name=_(u"Calle"))
    block = models.CharField(null=True, max_length=50, verbose_name=_(u"Colonia"))
    postal_code = models.CharField(null=True, max_length=50, verbose_name=_(u"Código postal"))
    municipality = models.CharField(null=True, max_length=50, verbose_name=_(u"Municipio"))
    state = models.CharField(null=True, max_length=50, verbose_name=_(u"Estado"))
    total_income = models.IntegerField(null=False, blank=False, default=1,
        choices=TOTAL_INCOME_BUCKET, verbose_name=_(u"Ingreso total"))

    comments = generic.GenericRelation(Comment)

    objects = ProspectionManager()

    def get_full_name(self):
        # Sometimes names are.. not there
        if not self.first_name:
            self.first_name = " "

        if not self.father_lastname:
            self.father_lastname = " "

        if not self.mother_lastname:
            self.mother_lastname = " "

        
        return u"%s %s %s" % (self.first_name, self.father_lastname, self.mother_lastname)

    def __unicode__(self):
        return "Vendedor: %s - Prospecto: %s" % (self.salesperson.first_name + " " + self.salesperson.last_name,
            self.get_full_name())
        
    class Meta:
        verbose_name = _(u"Prospección")
        verbose_name_plural = _(u"Prospecciones")


class PhoneLabel(models.Model):
    name = models.CharField(blank=False, max_length=50, verbose_name=_(u"Etiqueta de teléfono"))

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name = _(u"Etiqueta de teléfono")
        verbose_name_plural = _(u"Etiquetas de teléfonos")


class PhoneNumber(models.Model):
    prospection = models.ForeignKey(Prospection, verbose_name=_(u"Prospección"))
    phone_label = models.ForeignKey(PhoneLabel, verbose_name=_(u"Etiqueta de teléfono"))
    phone_number = models.CharField(max_length=20, null=False, blank=False,
        verbose_name=_(u"Número telefónico"))

    def __unicode__(self):
        return u"%s :: %s :: %s" % (self.prospection.first_name + " " + self.prospection.father_lastname,
            self.phone_label.name, self.phone_number)

    class Meta:
        verbose_name = _(u"Número telefónico")
        verbose_name_plural = _(u"Números telefónicos")
