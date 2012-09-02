from django.db import models
from apps.account.models import Profile
from django.contrib.contenttypes import generic
from apps.comment.models import Comment
from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _


PROSPECTION_STATUS_CHOICES = (
	(u"not qualfied", _(u"Not qualified")),
	(u"about to close", _(u"About to close")),
	(u"uninterested", _(u"Uninterested")),
	(u"layaway", _(u"Layaway")),
	(u"canceled", _(u"Canceled")),
)


PROSPECTION_FINANCIAL_OPTIONS = (
	("imss", _(u"IMSS")),
	("fovissste", _(u"FOVISSSTE")),
	("ipjal", _(u"IPJAL")),
	("no cotiza", _(u"No Cotiza")),
)


class ProspectionMedia(models.Model):
	name = models.CharField(blank=False, null=False, max_length=50, 
		verbose_name=_(u"Name"))


	def __unicode__(self):
		return u"%s" % self.name


	class Meta:
		verbose_name = _(u"Prospection media")
		verbose_name_plural = _(u"Prospection media")


class ProspectionChannel(models.Model):
	media = models.ForeignKey(ProspectionMedia, verbose_name=_(u"Media"))
	value = models.CharField(blank=False, null=False, max_length=50, 
		verbose_name=_(u"Value"))


	def __unicode__(self):
		return u"%s" % self.media.name


	class Meta:
		verbose_name = _(u"Prospection channel")
		verbose_name_plural = _(u"Prospection channels")


class Prospection(models.Model):
	salesperson = models.ForeignKey(User, blank=False, null=False,
		verbose_name=_(u'Salesperson'), related_name="salesperson", limit_choices_to={"is_staff": True})
	prospect = models.ForeignKey(Profile, blank=False, null=False, 
		verbose_name=_(u"Client"), related_name="prospect")

	# financial_channel = models.ForeignKey(FinancialChannelProspection, verbose_name=_(u"Financial channel"))

	financial_channel = models.CharField(blank=False, null=False, 
		verbose_name=_(u"Canal Financiero"), max_length=50, choices=PROSPECTION_FINANCIAL_OPTIONS)


	visitation_date = models.DateField(blank=False, null=False)
	status = models.CharField(blank=False, null=False, max_length=50, 
		verbose_name=_(u"Status"), choices=PROSPECTION_STATUS_CHOICES)

	comments = generic.GenericRelation(Comment)


	def __unicode__(self):
		return "%s - %s" % (self.salesperson.username, self.prospect.first_name + " " + self.prospect.father_lastname)


	class Meta:
		verbose_name = _(u"Prospection")
		verbose_name_plural = _(u"Prospections")