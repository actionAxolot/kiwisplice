# -*- coding: utf-8 -*-
from django.db import models
from apps.prospection.models import Prospection
from apps.inventory.models import Inventory
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic
from apps.comment.models import Comment
from django.db.models.signals import pre_save, post_save
import datetime


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
        return super(ClientManager, self).get_query_set()


# Create your models here.
class Client(models.Model):
    """ Whenever a prospection is aproved a client object is appended """
    prospection = models.ForeignKey(Prospection,
        verbose_name=_(u"Prospección"))
    inventory = models.ForeignKey(Inventory,
        unique=True, verbose_name=_(u"Inmueble"), null=True, blank=True)
    integration_date = models.DateField(null=True, blank=True, verbose_name=_(u"Integration date"))
    signature_date = models.DateField(null=True, blank=True, verbose_name=_(u"Signature date"))
    auth_date = models.DateField(null=True, blank=True, verbose_name=_(u"Authorization date"))
    pricing_date = models.DateField(null=True, blank=True, verbose_name=_(u"Pricing date"))
    payment_date = models.DateField(null=True, blank=True, verbose_name=_(u"Payment date"))
    notary = models.CharField(null=True, blank=True, verbose_name=_(u"Notary"), max_length=50)
    delivery_date = models.DateField(null=True, blank=True, verbose_name=_(u"Delivery date"))

    # Store the date in which this Client entry was created
    created_date = models.DateField(verbose_name=u'Fecha de creación')

    status = models.CharField(blank=False, null=False,
        choices=CLIENT_STATUS, max_length=50, default=_(u"Integración"),
        verbose_name=_(u"Status"))

    comments = generic.GenericRelation(Comment)

    def save(self, *args, **kwargs):
        """ On save update timestamps """
        if not self.id:
            self.created_date = datetime.date.today()
        super(Client, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"%s" % self.prospection.get_full_name()

    class Meta:
        verbose_name = _(u"Client")
        verbose_name_plural = _(u"Clients")


def delete_commissions(sender, instance, created, **kwargs):
    """
    Delete commissions when client is canceled
    """
    if not created:
        # Editing already existing record
        if instance.status == u"Cancelado":
            instance.commission_set.all().delete()


post_save.connect(delete_commissions, sender=Client)
