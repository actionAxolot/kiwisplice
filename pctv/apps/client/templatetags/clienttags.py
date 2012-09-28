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
def count_by_quincena(obj, date=None):
    # if date:
    #     # Convert the date param into a normal date
    #     quincena = date[0]
    #     month = MONTHS[date[7:]]

    #     # TODO: Dude this fucking sucks. Fix it later or delegate
    #     if month == 1:
    #         year = 2013
    #     else:
    #         year = 2012
    #     real_date = datetime.date(year, month, )
    return 20