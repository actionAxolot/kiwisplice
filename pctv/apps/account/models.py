# -*- coding: <utf-8> -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
import datetime

# Account module for PCTV software
class Profile(models.Model):
	""" Extension of the user model """
	user = models.OneToOneField(User, verbose_name=_(u"user"))

	# Things to know... just in case...
	street = models.CharField(null=True, max_length=50, verbose_name=_(u"Street"))
	block = models.CharField(null=True, max_length=50, verbose_name=_(u"Block"))
	postal_code = models.CharField(null=True, max_length=50, verbose_name=_(u"Postal code"))
	municipality = models.CharField(null=True, max_length=50, verbose_name=_(u"Municipality"))
	state = models.CharField(null=True, max_length=50, verbose_name=_(u"State"))
	total_income = models.DecimalField(null=True, max_digits=20, decimal_places=2, verbose_name=_(u"Total income"))

	def __unicode__(self):
		return u"%s %s" % (self.user.first_name, self.user.last_name)

	class Meta:
		verbose_name = _(u"Profile")
		verbose_name_plural = _(u"Profiles")


class PhoneLabel(models.Model):
	name = models.CharField(blank=False, max_length=50, verbose_name=_(u"Phone label"))


	def __unicode__(self):
		return u"%s" % self.name

	class Meta:
		verbose_name = _(u"Phone label")
		verbose_name_plural = _(u"Phone labels")


class PhoneNumber(models.Model):
	profile = models.ForeignKey(Profile, verbose_name=_(u"Profile"))
	phone_label = models.ForeignKey(PhoneLabel, verbose_name=_(u"Phone label"))
	phone_number = models.CharField(max_length=20, null=False, blank=False, 
		verbose_name=_(u"Phone number"))


	def __unicode__(self):
		return u"%s:%s:%s" % (self.profile.user.first_name +" "+ self.profile.user.last_name, 
			self.phone_label.name, self.phone_number)


	class Meta:
		verbose_name = _(u"Phone number")
		verbose_name_plural = _(u"Phone numbers")


def create_user_profile(sender, instance, created, **kwargs):
	if created:
		profile, created = Profile.objects.get_or_create(user=instance)


post_save.connect(create_user_profile, sender=User)