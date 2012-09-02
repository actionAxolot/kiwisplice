from django.db import models
from django.utils.translation import ugettext_lazy as _
from apps.inventory.models import Inventory
from apps.client.models import Client
from apps.prospection.models import Prospection


FINANCIAL_STATUS = (
	("pending", _(u"Pending")),
	("processing", _(u"Processing")),
	("rejected", _(u"Rejected")),
	("Canceled", _(u"Canceled")),
)


class FinancialInstitution(models.Model):
	name = models.CharField(blank=False, null=False, max_length=50, verbose_name=_(u"Name"))

	def __unicode__(self):
		return u"%s" % self.name

	class Meta:
		verbose_name = _(u"Financial institution")
		verbose_name_plural = _(u"Financial Institutions")


class FinancialChannelInventory(models.Model):
	inventory = models.ForeignKey(Inventory, verbose_name=_(u"Inventory"))

	financial_institution = models.ForeignKey(FinancialInstitution, 
		verbose_name=_(u'Financial institution'))

	status = models.CharField(null=False, blank=False, default="pending", 
		verbose_name=_(u"Status"), max_length=50, choices=FINANCIAL_STATUS)

	# Assign a score so that you can measure salespeople eficiency
	amount = models.DecimalField(blank=True, null=False, default=0, max_digits=10, decimal_places=2,
		verbose_name=_(u'Amount'))


	def __unicode__(self):
		return u"%s" % self.financial_institution.name


	class Meta:
		verbose_name = _(u"Financial channel for inventory")
		verbose_name_plural = _(u"Financial channels for inventory")



class FinancialChannelProspection(models.Model):
	financial_institution = models.ForeignKey(FinancialInstitution, 
		verbose_name=_(u'Financial institution'))


	prospection = models.ForeignKey(Prospection, verbose_name=_(u"Prospection"))


	status = models.CharField(null=False, blank=False, default="pending", 
		verbose_name=_(u"Status"), max_length=50, choices=FINANCIAL_STATUS)

	# Somersault


	# Assign a score so that you can measure salespeople eficiency
	amount = models.DecimalField(blank=True, null=False, default=0, max_digits=10, decimal_places=2,
		verbose_name=_(u'Amount'))


	def __unicode__(self):
		return u"%s" % self.financial_institution.name


	class Meta:
		verbose_name = _(u"Canal financiero para prospeccion")
		verbose_name_plural = _(u"Canal financiero para prospeccion")


# TODO: Remove this. Is legacy
class FinancialChannelClient(models.Model):
	client = models.ForeignKey(Client, verbose_name=_(u"Client"))

	financial_institution = models.ForeignKey(FinancialInstitution, 
		verbose_name=_(u'Financial institution'))

	status = models.CharField(null=False, blank=False, default="pending", 
		verbose_name=_(u"Status"), max_length=50, choices=FINANCIAL_STATUS)

	# Assign a score so that you can measure salespeople eficiency
	amount = models.DecimalField(blank=True, null=False, default=0, max_digits=10, decimal_places=2,
		verbose_name=_(u'Amount'))


	def __unicode__(self):
		return u"%s" % self.financial_institution.name


	class Meta:
		verbose_name = _(u"Financial channel for clients")
		verbose_name_plural = _(u"Financial channels for clients")