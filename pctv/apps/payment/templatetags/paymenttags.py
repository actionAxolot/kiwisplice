from django import template
from django.db.models import Sum
from apps.utils import MONTHS_DICT

register = template.Library()

def split_date(date):
    tokens = date.split(" ")
    month, year = tokens
    return month, year


@register.filter()
def get_by_month(qs, date=None):
    if date:
        month, year = split_date(date)
        return len(qs.filter(payment__date_due__month=MONTHS_DICT[month], payment__date_due__year=year))
    else:
        # Get the status of the qs
        return len(qs)


@register.filter()
def get_quantity_by_month(qs, date=None):
    if date:
        month, year = split_date(date)
        total = qs.filter(payment__date_due__month=MONTHS_DICT[month], payment__date_due__year=year).aggregate(
            total=Sum("payment__amount"))["total"]
        if total:
            return total
        else:
            return 0.00
    else:
        total = qs.aggregate(total=Sum("payment__amount"))["total"]
        if total:
            return total
        else:
            return 0.00