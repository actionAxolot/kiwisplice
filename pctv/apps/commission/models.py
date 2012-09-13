from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User
from apps.comment.models import Comment

COMMISSION_STATUS = (
	("pending", _(u"Pending")),
	("payed", _(u"Payed")),
	("about to cancel", _(u"About to cancel")),
)


class Commission(models.Model):
	salesperson = models.ForeignKey(User, verbose_name=_(u"Vendedor"))
	payment_date = models.DateField(blank=False, null=False, verbose_name=_(u"Payment date"))
	percentage = models.DecimalField(blank=False, null=False, verbose_name=_(u"Percentage"), 
		decimal_places=2, max_digits=5)
	status = models.CharField(blank=False, null=False, choices=COMMISSION_STATUS, 
		max_length=50, verbose_name=_(u"Status"))

	comment = generic.GenericRelation(Comment)


	class Meta:
		verbose_name = _(u"Commission")
		verbose_name_plural = _(u"Commissions")