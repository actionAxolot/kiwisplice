# -*- coding: <utf-8> -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
import datetime
import random
import datetime

# PROSPECTION_USER = User.objects.get(username="prospecciones")

# Account module for PCTV software
class Profile(models.Model):
	""" Extension of the user model """
	user = models.OneToOneField(User, blank=True, null=False, default=1, verbose_name=_(u"user"))


	def __unicode__(self):
		return u"Perfil para %s" % (self.user.username,)


	class Meta:
		verbose_name = _(u"Profile")
		verbose_name_plural = _(u"Profiles")


def create_user_profile(sender, instance, created, **kwargs):
	if created:
		profile, created = Profile.objects.get_or_create(user=instance)


post_save.connect(create_user_profile, sender=User)