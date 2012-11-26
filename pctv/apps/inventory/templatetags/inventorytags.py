# -*- coding: utf-8 -*-
from django import template
from django.db.models import Sum

MONTHS = {
    "ENERO": 1,
    "FEBRERO": 2,
    "MARZO": 3,
    "ABRIL": 4,
    "MAYO": 5,
    "JUNIO": 6,
    "JULIO": 7,
    "AGOSTO": 8,
    "SEPTIEMBRE": 9,
    "OCTUBRE": 10,
    "NOVIEMBRE": 11,
    "DICIEMBRE": 12,
}

register = template.Library()

@register.filter()
def get_earned_total(qs):
    total = qs.filter(client__payment_date__isnull=False).aggregate(total=Sum("client__payment__amount"))["total"]
    if not total:
        total = u"No cuenta con pagos"

    return total

@register.filter()
def count_by_month(obj, date=None):
    if date:
        # Get the date into tokents
        tokens = date.split(" ")
        month, year = tokens

        month = MONTHS[month]

        # Now count how many are 
        return len(obj.filter(construction_end_date__month=month, construction_end_date__year=year))

    return len(obj)


@register.filter()
def count_by_status(obj, status=None):
    if status:
        return len(obj.filter(construction_status=status))
    else:
        return len(obj)
