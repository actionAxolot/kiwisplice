from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic

from apps.client.models import Client
from apps.comment.models import Comment


PAYMENT_STATUS = (
	("Actual", _("Actual")),
	("Pagado", _("Pagado")),
	("Vencido", _("Vencido")),
)


class Payment(models.Model):
    client = models.ForeignKey(Client, verbose_name=_(u"Cliente"))
    amount = models.DecimalField(blank=False, null=False,
				 max_digits=20, decimal_places=2, verbose_name=_("Amount"))
    date_due = models.DateField(blank=False, null=True, verbose_name=_("Date due"))
    date_payed = models.DateField(blank=True, null=True, verbose_name=_("Date payed"))
    status = models.CharField(max_length=30, blank=True, null=True, default="Actual", verbose_name=_("Status"), choices=PAYMENT_STATUS)

    comments = generic.GenericRelation(Comment)

    class Meta:
        verbose_name = _("Payment")
	verbose_name_plural = _("Payments")
