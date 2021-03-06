# -*- coding: utf-8 -*-
from django import template
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


def get_date_data(date):
    tokens = date.split(" ")
    month, year = tokens
    return month, year

# The following two are pretty much the same. Still looking for a nice solution
@register.filter()
def count_by_month_clients(obj, date=None):
    if isinstance(date, str):
        # Get the date into tokents
        month, year = get_date_data(date)
        month = MONTHS[month]

        # Now count how many are
        return len(obj.filter(created_date__month=month, created_date__year=year))

    obj_total = 0
    for m in date:
        month, year = get_date_data(m)
        month = MONTHS[month]
        obj_total += len(obj.filter(created_date__month=month, created_date__year=year))

    return obj_total


@register.filter()
def count_by_month_prospections(obj, date=None):
    if isinstance(date, str):
        # Get the date into tokents
        month, year = get_date_data(date)
        month = MONTHS[month]

        # Now count how many are
        return len(obj.filter(visitation_date__month=month, visitation_date__year=year))

    obj_total = 0
    for m in date:
        month, year = get_date_data(m)
        month = MONTHS[month]
        obj_total += len(obj.filter(visitation_date__month=month, visitation_date__year=year))

    return obj_total
