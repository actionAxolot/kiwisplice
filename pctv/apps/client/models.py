# -*- coding: utf-8 -*-
from django.db import models
from apps.prospection.models import Prospection
from apps.inventory.models import Inventory
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic
from apps.comment.models import Comment
from django.db.models.signals import pre_save, post_save


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


class ClientManager(models.Manager):
    def get_query_set(self, *args, **kwargs):
        # Return the ones that are not canceled
        return super(ClientManager, self).get_query_set().exclude(status=u"Cancelado")


# Create your models here.
class Client(models.Model):
    """ Whenever a prospection is aproved a client object is appended """
    prospection = models.ForeignKey(Prospection, 
        verbose_name=_(u"Prospección"), limit_choices_to={"status__in": ("Apartado", "Por cerrar")})
    inventory = models.ForeignKey(Inventory,
                                  limit_choices_to={"construction_status__in": (u"Libre", u"Con cliente")},
                                  unique=True, verbose_name=_(u"Inmueble"))
    integration_date = models.DateField(null=True, blank=True, verbose_name=_(u"Integration date"))
    signature_date = models.DateField(null=True, blank=True, verbose_name=_(u"Signature date"))
    auth_date = models.DateField(null=True, blank=True, verbose_name=_(u"Authorization date"))
    pricing_date = models.DateField(null=True, blank=True, verbose_name=_(u"Pricing date"))
    payment_date = models.DateField(null=True, blank=True, verbose_name=_(u"Payment date"))
    notary = models.CharField(null=True, blank=True, verbose_name=_(u"Notary"), max_length=50)
    delivery_date = models.DateField(null=True, blank=True, verbose_name=_(u"Delivery date"))

    status = models.CharField(blank=False, null=False, 
        choices=CLIENT_STATUS, max_length=50, default=_(u"Integración"),
        verbose_name=_(u"Status"))

    comments = generic.GenericRelation(Comment)

    def __unicode__(self):
        return u"%s" % self.prospection.get_full_name()

    class Meta:
        verbose_name = _(u"Client")
        verbose_name_plural = _(u"Clients")


def free_inventory_status(sender, instance, **kwargs):
    """
    Check the status according to whatever we are catching
    """
    try:
        if instance.inventory:
            # This means it already has an inventory.
            # Get whatever's in the DB right now
            client = Client.objects.filter(pk=instance.pk)[0]
            client.inventory.construction_status = u"Libre"
            client.inventory.save()
    except:
        pass


def set_inventory_status(sender, instance, created, **kwargs):
    try:
        if instance.inventory:
            # An inventory was set
            instance.inventory.construction_status = u"Con cliente"
            instance.inventory.save()
    except:
        pass


pre_save.connect(free_inventory_status, sender=Client)
post_save.connect(set_inventory_status, sender=Client)
