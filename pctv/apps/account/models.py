# -*- coding: <utf-8> -*-
from django.db import models
from django.contrib.auth.models import User
from apps.financial_channel.models import FinancialChannel
from apps.prospection_channel.models import ProspectionChannel
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
import datetime

# Account module for PCTV software
class Profile(models.Model):
	user = models.OneToOneField(User, verbose_name=_("user"))
	salesman = models.ForeignKey(User, related_name='salesman', 
		verbose_name_("salesperson"))
	visitation_date = models.DateTimeField(blank=False, null=False, default=datetime.datetime.today(),
		verbose_name=_("visitation date"))
	street = models.CharField(max_length=300, blank=False, null=False, 
		verbose_name=_("street"))
	block = models.CharField(max_length=300, blank=False, null=False, 
		verbose_name=_("block"))
	postal_code = models.IntegerField(blank=False, null=False, 
		verbose_name=_("postal code"))
	municipality = models.CharField(max_length=300, blank=False, null=False, 
		verbose_name=_("municipality"))
	state = models.CharField(max_length=100, blank=False, null=False, 
		verbose_name=_("state"))
	phone = models.CharField(max_length=100, blank=False, null=False,
		verbose_name=_("phone"))
	mobile = models.CharField(max_length=100, blank=False, null=False,
		verbose_name=_("mobile"))
	emergency_phone = models.CharField(max_length=100, blank=False, null=False, 
		verbose_name=_("emergency phone"))
	total_income = models.DecimalField(max_digits=14, decimal_places=2, blank=False, null=False,
		verbose_name=_("total income"))

	financial_channel = models.ForeignKey(FinancialChannel, verbose_name=_("financial channel"))
	prospection_channel = models.ForeignKey(ProspectionChannel, verbose_name=_("prospection channel"))

	def __unicode__(self):
		return _(u"%s's profile" % self.user)

	class Meta:
		verbose_name = _(u"Profile")
		verbose_name_plural = _(u"Profiles")


class ClientComments(models.Model):
	"""Whatever"""
	user = models.ForeignKey(Profile)
	comment = models.TextField()


def create_user_profile(sender, instance, created, **kwargs):
	if created:
		profile, created = Profile.objects.get_or_create(user=instance)


# post_save.connect(create_user_profile, sender=User)