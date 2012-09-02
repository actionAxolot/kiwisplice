from django.db import models
from apps.account.models import Profile
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
	profile = models.ForeignKey(Profile, verbose_name=_(u"Profile"))
	integration_date = models.DateField(null=True, verbose_name=_(u"Integration date"))
	signature_date = models.DateField(null=True, verbose_name=_(u"Signature date"))
	auth_date = models.DateField(null=True, verbose_name=_(u"Authorization date"))
	pricing_date = models.DateField(null=True, verbose_name=_(u"Pricing date"))
	payment_date = models.DateField(null=True, verbose_name=_(u"Payment date"))
	notary = models.CharField(null=True, verbose_name=_(u"Notary"), max_length=50)
	delivery_date = models.DateField(null=True, verbose_name=_(u"Delivery date"))

	# TODO: Comments... I think you won't have to add anything here for that to work
	status = models.CharField(blank=False, null=False, choices=CLIENT_STATUS, max_length=50, 
		verbose_name=_(u"Status"))

	comments = generic.GenericRelation(Comment)

	class Meta:
		verbose_name = _(u"Client")
		verbose_name_plural = _(u"Clients")