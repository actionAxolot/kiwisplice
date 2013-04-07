# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User
from apps.client.models import Client
from django.shortcuts import redirect

# We are gonna use signals... not sure why
from django.db.models.signals import post_save

# Utils and stuff
import datetime

COMMISSION_STATUS = (
	("Pendiente", _(u"Pendiente")),
	("Pagado", _(u"Pagado")),
        ("Cancelado", _(u"Cancelado")),
)


class Commission(models.Model):
    client = models.ForeignKey(Client, verbose_name=_(u"Cliente"))
    created_date = models.DateTimeField(auto_now=True,
                                        verbose_name=_(u"Fecha creación"))
    modified_date = models.DateTimeField(auto_now_add=True,
                                         verbose_name=_(u"Fecha modificación"))
    status = models.CharField(blank=False, null=False, choices=COMMISSION_STATUS,
        max_length=50, verbose_name=_(u"Status"), default="Pendiente")

    def __unicode__(self):
        return u"%s" % self.client

    class Meta:
        verbose_name = _(u"Comision")
        verbose_name_plural = _(u"Comisiones")


class CommissionPayment(models.Model):
    commission = models.ForeignKey(Commission, verbose_name=_(u"Pago de comisión"))
    percentage = models.DecimalField(blank=False, null=False, verbose_name=_(u"Porcentaje"),
        decimal_places=2, max_digits=5)
    payment_date = models.DateField(blank=True, null=True, verbose_name=_(u"Fecha de pago"))
    status = models.CharField(max_length=15, blank=False, null=False,
                              default="Pendiente", choices=((u"Pendiente", u"Pendiente"),
                                                            (u"Por pagar", u"Por pagar"),
                                                            (u"Pagado", u"Pagado")))

    def __unicode__(self):
        return u"Pagar a %s" % self.commission.client.prospection.salesperson


def create_commission(sender, instance, created, **kwargs):
    def create_payments(commission):
        CommissionPayment(commission=commission, percentage=0.20).save()
        CommissionPayment(commission=commission, percentage=0.20).save()
        CommissionPayment(commission=commission, percentage=0.60).save()

    if created:
        # If the client was just created raise the three necessary payments
        commission = Commission(client=instance)
        commission.save()
        create_payments(commission)
    else:
        # Did the client generate commissions already?
        try:
            commission = Commission.objects.get(client=instance)
        except Commission.DoesNotExist:
            commission = Commission(client=instance)
            commission.save()
            create_payments(commission)
        # Check if payments have been generated... could be an old record or something

        two_weeks = datetime.date.today() + datetime.timedelta(days=15)
        if instance.status == "Cancelado":
            commission.status = "Cancelado"
            commission.save()
        elif instance.status == "Pre-autorizado":
            payment = commission.commissionpayment_set.all().order_by("id")[0]
            payment.status = "Por pagar"
            payment.payment_date = two_weeks
            payment.save()
        elif instance.status == "Autorizado":
            payment = commission.commissionpayment_set.all().order_by("id")[1]
            payment.status = "Por pagar"
            payment.payment_date = two_weeks
            payment.save()
        elif instance.status == "Firmado":
            payment = commission.commissionpayment_set.all().order_by("id")[2]
            payment.status = "Por pagar"
            payment.payment_date = two_weeks
            payment.save()


# Now we connect the signal
post_save.connect(create_commission, sender=Client)
