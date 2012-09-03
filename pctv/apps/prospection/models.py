# -*- coding: utf-8 -*-
from django.db import models
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
		verbose_name=_(u'Salesperson'), related_name="salesperson")
	financial_channel = models.CharField(blank=False, null=False, 
		verbose_name=_(u"Canal Financiero"), max_length=50, choices=PROSPECTION_FINANCIAL_OPTIONS)
	visitation_date = models.DateField(blank=False, null=False)
	status = models.CharField(blank=False, null=False, max_length=50, 
		verbose_name=_(u"Status"), choices=PROSPECTION_STATUS_CHOICES)


	# Things to know... just in case...
	first_name = models.CharField(blank=False, null=False, max_length=50, verbose_name=_(u"First name"))
	middle_name = models.CharField(blank=False, null=True, max_length=50, verbose_name=_(u"Middle name"))
	father_lastname = models.CharField(blank=False, null=False, max_length=50, verbose_name=_(u"Father's last name"))
	mother_lastname = models.CharField(blank=False, null=True, max_length=50, verbose_name=_(u"Mother's last name"))
	email = models.CharField(blank=False, null=False, max_length=50, verbose_name=_(u"Email"))

	street = models.CharField(null=True, max_length=50, verbose_name=_(u"Street"))
	block = models.CharField(null=True, max_length=50, verbose_name=_(u"Block"))
	postal_code = models.CharField(null=True, max_length=50, verbose_name=_(u"Postal code"))
	municipality = models.CharField(null=True, max_length=50, verbose_name=_(u"Municipality"))
	state = models.CharField(null=True, max_length=50, verbose_name=_(u"State"))
	total_income = models.DecimalField(null=True, max_digits=20, decimal_places=2, verbose_name=_(u"Total income"))


	comments = generic.GenericRelation(Comment)


	def __unicode__(self):
		return "%s - %s" % (self.first_name, self.father_lastname + " " + self.mother_lastname)


	class Meta:
		verbose_name = _(u"Prospection")
		verbose_name_plural = _(u"Prospections")


class PhoneLabel(models.Model):
	name = models.CharField(blank=False, max_length=50, verbose_name=_(u"Phone label"))

	def __unicode__(self):
		return u"%s" % self.name

	class Meta:
		verbose_name = _(u"Phone label")
		verbose_name_plural = _(u"Phone labels")


class PhoneNumber(models.Model):
	prospection = models.ForeignKey(Prospection, verbose_name=_(u"Prospección"))
	phone_label = models.ForeignKey(PhoneLabel, verbose_name=_(u"Phone label"))
	phone_number = models.CharField(max_length=20, null=False, blank=False, 
		verbose_name=_(u"Phone number"))


	def __unicode__(self):
		return u"%s:%s:%s" % (self.profile.user.first_name +" "+ self.profile.user.last_name, 
			self.phone_label.name, self.phone_number)


	class Meta:
		verbose_name = _(u"Phone number")
		verbose_name_plural = _(u"Phone numbers")