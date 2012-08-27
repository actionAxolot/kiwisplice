from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic
from apps.payment.models import PaymentGroup
from apps.comment.models import Comment

COMMISSION_STATUS = (
	("pending", _(u"Pending")),
	("payed", _(u"Payed")),
	("about to cancel", _(u"About to cancel")),
)


class CommissionGroup(models.Model):
	payment_group = models.ForeignKey(PaymentGroup, verbose_name=_(u"Payment group"))
	cancellation_date = models.DateField(blank=True, null=True, 
		verbose_name=_(u"Cancellation date"))

	comments = generic.GenericRelation(Comment)


	class Meta:
		verbose_name = _(u"Commission group")
		verbose_name_plural = _(u"Commission groups")


class Commission(models.Model):
	commission_group = models.ForeignKey(CommissionGroup, verbose_name=_(u"Commission group"))
	payment_date = models.DateField(blank=False, null=False, verbose_name=_(u"Payment date"))
	percentage = models.DecimalField(blank=False, null=False, verbose_name=_(u"Percentage"), 
		decimal_places=2, max_digits=5)
	status = models.CharField(blank=False, null=False, choices=COMMISSION_STATUS, 
		max_length=50, verbose_name=_(u"Status"))

	comment = generic.GenericRelation(Comment)


	class Meta:
		verbose_name = _(u"Commission")
		verbose_name_plural = _(u"Commissions")