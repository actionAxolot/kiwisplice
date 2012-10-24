# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import unicodedata


# Create your models here.
class Role(models.Model):
	user = models.ManyToManyField(User, null=True, blank=True, verbose_name=u'Usuario')
	name = models.CharField(blank=False, null=False, max_length=50, verbose_name=u'Etiqueta')
	slug = models.CharField(blank=True, null=True, max_length=50)

	def save(self, *args, **kwargs):
		"""
		Just create a slug by changing spaces to underscores, removing special characters
		and and making everything lowercase
		"""
		# Cleanup name string to slugify  
		clean_string = self.name.replace(" ", "-")
		clean_string = ''.join((c for c in unicodedata.normalize('NFD', clean_string) if unicodedata.category(c) != "Mn"))
		self.slug = clean_string.lower()

		super(Role, self).save(*args, **kwargs)

	def __unicode__(self):
		return u"%s" % self.name

	class Meta:
		verbose_name = u"Rol"
		verbose_name_plural = u"Roles"