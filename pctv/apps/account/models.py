from django.db import models
from django.contrib.auth.models import User
from apps.financial_channel.models import FinancialChannel
from apps.prospection_channel.models import ProspectionChannel
from django.db.models.signals import post_save
import datetime

# Account module for PCTV software
class Profile(models.Model):
	user = models.OneToOneField(User)
	salesman = models.ForeignKey(User, related_name='salesman')
	visitation_date = models.DateTimeField(blank=False, null=False, default=datetime.datetime.today())
	street = models.CharField(max_length=300, blank=False, null=False)
	block = models.CharField(max_length=300, blank=False, null=False)
	postal_code = models.IntegerField(blank=False, null=False)
	municipality = models.CharField(max_length=300, blank=False, null=False)
	state = models.CharField(max_length=100, blank=False, null=False)
	phone = models.CharField(max_length=100, blank=False, null=False)
	mobile = models.CharField(max_length=100, blank=False, null=False)
	emergency_phone = models.CharField(max_length=100, blank=False, null=False)
	total_income = models.DecimalField(max_digits=14, decimal_places=2, blank=False, null=False)

	financial_channel = models.ForeignKey(FinancialChannel)
	prospection_channel = models.ForeignKey(ProspectionChannel)

	def __unicode__(self):
		return u"%s's profile" % self.user


class ClientComments(models.Model):
	"""Whatever"""
	user = models.ForeignKey(Profile)
	comment = models.TextField()


def create_user_profile(sender, instance, created, **kwargs):
	if created:
		profile, created = Profile.objects.get_or_create(user=instance)


# post_save.connect(create_user_profile, sender=User)