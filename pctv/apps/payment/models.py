from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic

from apps.client.models import Client
from apps.comment.models import Comment


PAYMENT_STATUS = (
	("current", _("Current")),
	("paid", _("Paid")),
	("late", _("Late")),
)


class PaymentGroup(models.Model):
	client = models.ForeignKey(Client, verbose_name=_("Client"))
	total = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2, verbose_name=_("Total"))
	date_created = models.DateField(blank=True, null=True, verbose_name=_("Date created"))
	date_closed = models.DateField(blank=True, null=True, verbose_name=_("Date closed"))

	comments = generic.GenericRelation(Comment)


	class Meta:
		verbose_name = _("Payment group")
		verbose_name_plural = _("Payment groups")


class Payment(models.Model):
	payment_group = models.ForeignKey(PaymentGroup, verbose_name=_("Payment group"))
	amount = models.DecimalField(blank=False, null=True, max_digits=20, decimal_places=2, verbose_name=_("Amount"))
	date_due = models.DateField(blank=False, null=True, verbose_name=_("Date due"))
	date_payed = models.DateField(blank=False, null=True, verbose_name=_("Date payed"))
	status = models.CharField(max_length=30, blank=True, null=True, verbose_name=_("Status"), choices=PAYMENT_STATUS)

	comments = generic.GenericRelation(Comment)


	class Meta:
		verbose_name = _("Payment")
		verbose_name_plural = _("Payments")