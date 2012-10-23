# -*- coding: utf-8 -*-
from django import template
from django.conf import settings
from decimal import Decimal

register = template.Library()


@register.filter()
def get_next_payment_date(commission):
    payments = commission.commissionpayment_set.filter(payment_date__isnull=False).order_by("-payment_date")
    try:
        return payments[0].payment_date
    except:
        return "En proceso"

@register.filter()
def get_commission_total(commission):
    price = commission.client.inventory.get_price()
    total_to_pay = price * Decimal(str(settings.COMMISSION_PERCENT))
    return u"%.2f" % total_to_pay

@register.filter()
def get_commission_payment_total(payment):
    commissionable_total = payment.commission.client.inventory.get_price() * Decimal(str(settings.COMMISSION_PERCENT))
    return u"%.2f" % (commissionable_total * payment.percentage)
