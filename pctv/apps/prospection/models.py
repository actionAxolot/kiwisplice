from django.db import models
from apps.account.models import Profile
from apps.inventory.models import FinancialInstitution

from django.utils.translation import ugettext_lazy as _


PROSPECTION_STATUS_CHOICES = (
	(u"not qualfied", _(u"Not qualified")),
	(u"about to close", _(u"About to close")),
	(u"uninterested", _(u"Uninterested")),
	(u"layaway", _(u"Layaway")),
	(u"canceled", _(u"Canceled")),
)


class FinancialChannel(models.Model):
	financial_institution = models.ForeignKey(FinancialInstitution, 
		verbose_name=_(u'Financial institution'))

	# Assign a score so that you can measure salespeople eficiency
	value = models.IntegerField(blank=True, null=False, default=0, 
		verbose_name=_(u'Value'))


	class Meta:
		verbose_name = _(u"Financial channel")
		verbose_name_plural = _(u"Financial channels")


class ProspectionMedia(models.Model):
	name = models.CharField(blank=False, null=False, max_length=50, 
		verbose_name=_(u"Name"))


	class Meta:
		verbose_name = _(u"Prospection media")
		verbose_name_plural = _(u"Prospection media")


class ProspectionChannel(models.Model):
	media = models.ForeignKey(ProspectionMedia, verbose_name=_(u"Media"))
	value = models.CharField(blank=False, null=False, max_length=50, 
		verbose_name=_(u"Value"))


	class Meta:
		verbose_name = _(u"Prospection channel")
		verbose_name_plural = _(u"Prospection channels")


class Prospection(models.Model):
	salesperson = models.ForeignKey(Profile, blank=False, null=False,
		verbose_name=_(u'Salesperson'), related_name="salesperson")
	prospect = models.ForeignKey(Profile, blank=False, null=False, 
		verbose_name=_(u"Client"), related_name="prospect")

	financial_channel = models.ForeignKey(FinancialChannel, verbose_name=_(u"Financial channel"))
	prospection_channel = models.ForeignKey(ProspectionChannel, verbose_name=_(u"Prospection channel"))

	visitation_date = models.DateField(blank=False, null=False)
	status = models.CharField(blank=False, null=False, max_length=50, 
		verbose_name=_(u"Status"), choices=PROSPECTION_STATUS_CHOICES)