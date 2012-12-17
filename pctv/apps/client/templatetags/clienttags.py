# -*- coding: utf-8 -*-
from django import template
import datetime

register = template.Library()

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

@register.filter()
def count_by_month(obj, date=None):
    if date:
        # Get the date into tokents
        tokens = date.split(" ")
        month, year = tokens

        month = MONTHS[month]

        # Now count how many are 
        return len(obj.filter(signature_date__month=month, signature_date__year=year))

    return len(obj)
