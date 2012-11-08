# -*- coding: utf-8 -*-
from django import template

register = template.Library()


@register.filter()
def count_by_status(obj, status=None):
    if status:
        return len(obj.filter(status=status))
    else:
        return len(obj)


@register.filter()
def translate_dictionary_key(key):
    return {
        0: "Recientes",
        1: "1 Semana",
        2: "2 Semanas",
        3: "3 Semanas",
        4: "4 Semanas",
        5: "5 Semanas",
        6: "6 Semanas",
        7: "7 Semanas",
        8: "8 Semanas",
    }.get(key, "2 Meses o más")


@register.filter()
def getkey(dict, key):
    return dict[key]


@register.filter()
def count_by_income(obj, income=None):
    if income:
        return len(obj.filter(total_income=income))
    else:
        return len(obj)


@register.filter()
def debug_shit(obj):
    import pdb; pdb.set_trace()
