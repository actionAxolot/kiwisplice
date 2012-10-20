# -*- coding: utf-8 -*-
from django.db import models
from apps.prospection.models import Prospection
from apps.inventory.models import Inventory
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic
from apps.comment.models import Comment


CLIENT_STATUS = (
    (u"Integración", _(u"Integración")),
    (u"Análisis", _(u"Análisis")),
    (u"Pre-autorizado", _(u"Pre-autorizado")),
    (u"Salvedad", _(u"Salvedad")),
    (u"Autorizado", _(u"Autorizado")),
    (u"Dictaminación", _(u"Dictaminación")),
    (u"Por firmar", _(u"Por firmar")),
    (u"Firmado", _(u"Firmado")),
    (u"Cobrado", _(u"Cobrado")),
    (u"Viv. Entregada", _(u"Viv. Entregada")),
    (u"Cancelado", _(u"Cancelado")),
)


# Create your models here.
class Client(models.Model):
    """ Whenever a prospection is aproved a client object is appended """
    prospection = models.ForeignKey(Prospection, 
        verbose_name=_(u"Prospección"), limit_choices_to={"status__in": ("Apartado", "Por cerrar")})
    inventory = models.ForeignKey(Inventory, verbose_name=_(u"Inmueble"), blank=True, null=True)
    integration_date = models.DateField(null=True, blank=True, verbose_name=_(u"Integration date"))
    signature_date = models.DateField(null=True, blank=True, verbose_name=_(u"Signature date"))
    auth_date = models.DateField(null=True, blank=True, verbose_name=_(u"Authorization date"))
    pricing_date = models.DateField(null=True, blank=True, verbose_name=_(u"Pricing date"))
    payment_date = models.DateField(null=True, blank=True, verbose_name=_(u"Payment date"))
    notary = models.CharField(null=True, blank=True, verbose_name=_(u"Notary"), max_length=50)
    delivery_date = models.DateField(null=True, blank=True, verbose_name=_(u"Delivery date"))

    status = models.CharField(blank=False, null=False, 
        choices=CLIENT_STATUS, max_length=50, default="Sin cliente",
        verbose_name=_(u"Status"))

    comments = generic.GenericRelation(Comment)

    def __unicode__(self):
        return u"%s - %s" %(self.prospection.get_full_name(), 
            self.prospection.salesperson.first_name + " " + self.prospection.salesperson.last_name)

    def save(self, *args, **kwargs):
        # Change status of the inventory to 'Con cliente'
        if self.pk:
            self.inventory.construction_status = u"Con cliente"
            self.inventory.save()
        super(Client, self).save(*args, **kwargs)
        


    class Meta:
        verbose_name = _(u"Client")
        verbose_name_plural = _(u"Clients")
