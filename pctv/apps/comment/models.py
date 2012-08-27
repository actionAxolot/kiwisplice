from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _
from apps.account.models import Profile


# Create your models here.
class Comment(models.Model):
	""" Comments on necessary stuff that needs comments """
	commenter = models.ForeignKey(Profile, verbose_name=_(u"Commenter"))
	text = models.TextField(verbose_name=_(u"Text"))
	content_type = models.ForeignKey(ContentType, verbose_name=_(u"Content type"))
	object_id = models.PositiveIntegerField(verbose_name=_(u"Object ID"))
	content_object = generic.GenericForeignKey('content_type', 'object_id')

	def __unicode__(self):
		return u"%s" % self.text


	class Meta:
		verbose_name = _(u"Comment")
		verbose_name_plural = _(u"Comments")