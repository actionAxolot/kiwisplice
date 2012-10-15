# -*- coding: utf-8 -*-
from django import template
from decimal import Decimal
import datetime

register = template.Library()


@register.filter
def bridge_credit_left(total, ministered):
    return total - ministered


@register.filter
def bridge_credit_owed(total, payed):
    return total - payed


@register.filter
def bridge_credit_ministered_percentage(total, ministered):
    return (ministered * 100) / Decimal(total)


@register.filter
def bridge_credit_left_percentage(total, ministered):
    ministered_percentage = (ministered * 100) / total
    return 100 - ministered_percentage


@register.filter
def format_time_spans(date):
    months = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto",
        "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]

    month = months[date.month - 1]
    day = date.day

    if day < 15:
        day = "1RA"
    else:
        day = "2DA"

    return u"%s de %s" % (day, month)


@register.filter
def days_from_now(date=None):
    if not date:
        return u"No hay fecha definida"
    today = datetime.date.today()
    difference = today - date
    if difference.days > 0:
        return "%s de %d dias" % ("Más", difference.days)
    else:
        return "%s de %d dias" % ("Menos", difference.days * -1)
