# -*- coding: utf-8 -*-
from django.db import models
from apps.prospection.models import Prospection
from apps.inventory.models import Inventory
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic
from apps.comment.models import Comment


CLIENT_STATUS = (
	("no client", _(u"No client")),
	("integration", _(u"Integration")),
	("preauthorization", _(u"Pre-authorization")),
	("analysis", _(u"Analysis")),
	("salvity", _(u"Salvity")),
	("authorized", _(u"Authorized")),
	("dictamination", _(u"Dictamination")),
	("about to sign", _(u"About to sign")),
	("signed", _(u"Signed")),
	("charged", _(u"Charged")),
	("delivered", _(u"Delivered")),
	("canceled", _(u"Canceled")),
)


# Create your models here.
class Client(models.Model):
	""" Whenever a prospection is aproved a client object is appended """
	prospection = models.ForeignKey(Prospection, 
		verbose_name=_(u"Prospección"), limit_choices_to={"status": "layaway"})
	inventory = models.ForeignKey(Inventory, 
		verbose_name=_(u"Inmueble"), limit_choices_to={"construction_status": "finished"},
		blank=True, null=True)
	integration_date = models.DateField(null=True, blank=True, verbose_name=_(u"Integration date"))
	signature_date = models.DateField(null=True, blank=True, verbose_name=_(u"Signature date"))
	auth_date = models.DateField(null=True, blank=True, verbose_name=_(u"Authorization date"))
	pricing_date = models.DateField(null=True, blank=True, verbose_name=_(u"Pricing date"))
	payment_date = models.DateField(null=True, blank=True, verbose_name=_(u"Payment date"))
	notary = models.CharField(null=True, blank=True, verbose_name=_(u"Notary"), max_length=50)
	delivery_date = models.DateField(null=True, blank=True, verbose_name=_(u"Delivery date"))

	status = models.CharField(blank=False, null=False, 
		choices=CLIENT_STATUS, max_length=50, default="no client",
		verbose_name=_(u"Status"))

	comments = generic.GenericRelation(Comment)

	def __unicode__(self):
		return u"%s - %s" %(self.prospection.get_full_name(), 
			self.prospection.salesperson.first_name + " " + self.prospection.salesperson.last_name)

	class Meta:
		verbose_name = _(u"Client")
		verbose_name_plural = _(u"Clients")