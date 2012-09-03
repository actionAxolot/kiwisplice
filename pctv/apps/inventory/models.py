from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User

from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType



# Porcentajes options... this is probably retardedr
PERCENTAGES_OPTIONS = tuple([(x, unicode(x) + u"%") for x in xrange(0, 110, 10)])


# How's the brige credit going?
BRIDGE_CREDIT_STATUSES = (
	(u"approved", _(u"Approved")),
	(u"not approved", _(u"Not approved")),
)

# Construction options
CONSTRUCTION_STATUS = (
	(u"building", _(u"Building")),
	(u"Approved and building", _(u"Approved and building")),
	(u"Finished", _(u"Finished")),
	(u"Blocked", _(u"Blocked")),
)

LOCATION_STATUS = (
	(u"free", _(u"Free")),
	(u"blocked", _(u"Blocked")),
)


class Prototype(models.Model):
	name = models.CharField(blank=False, null=False, max_length=50, verbose_name=_(u'Name'))
	image = models.ImageField(upload_to="prototype_pics", null=True, blank=True, verbose_name=_(u"Image"))
	price = models.CharField(blank=False, null=False, max_length=50, verbose_name=_(u"Price"))


	def __unicode__(self):
		return u"%s" % (self.name,)


	class Meta:
		verbose_name = _(u"Prototype")
		verbose_name_plural = _(u"Prototypes")


# Create your models here.
class Section(models.Model):
	name = models.CharField(blank=False, null=False, 
		max_length=50, verbose_name=_(u"Name"))


	def __unicode__(self):
		return u"%s" % self.name


	class Meta:
		verbose_name = _(u'Section')
		verbose_name_plural = _(u'Sections')


class Inventory(models.Model):
	""" What houses are / will be available? """
	created_by = models.ForeignKey(User, verbose_name=_(u'Created by'))
	prototype = models.ForeignKey(Prototype, verbose_name=_(u'Prototype'))
	section = models.ForeignKey(Section, verbose_name=_(u"Section"))
	construction_status = models.CharField(max_length=40, blank=False, null=False, 
		choices=CONSTRUCTION_STATUS, verbose_name=_(u"Construction status"))
	location_status = models.CharField(blank=False, null=False, 
		max_length=50, verbose_name=_(u"Location Status"), choices=LOCATION_STATUS)
	cuv = models.CharField(max_length=200, blank=True, null=False, verbose_name=_(u'CUV'), )
	official_id = models.CharField(max_length=200, blank=False, null=False, verbose_name=_(u"Official Identifier"))

	# TODO: This one should be filled automatically
	unique_id = models.CharField(max_length=50, blank=True, null=True, 
		verbose_name=_(u"Unique identifier (Block + Macrolot + Lot)"))
	block = models.CharField(max_length=50, blank=False, null=False, verbose_name=_(u'Block'))
	macro_lot = models.CharField(blank=False, null=False, 
		verbose_name=_(u'Macro lot'), max_length=50)
	lot = models.CharField(blank=False, null=False, 
		verbose_name=_(u'Lot'), max_length=50)
	street = models.CharField(blank=False, null=False, 
		verbose_name=_(u"Street"), max_length=50)
	number = models.CharField(blank=False, null=False, 
		verbose_name=_(u'Realestate number'), max_length=50)
	lot_size = models.IntegerField(blank=False, null=False, verbose_name=_(u"Lot size"))
	construction_size = models.IntegerField(blank=False, null=False, verbose_name=_(u'Construction size'))
	construction_end_date = models.DateField(blank=False, null=False, verbose_name=_(u"Construction end date"))
	percent_completed = models.IntegerField(blank=False, null=False, 
		default=0, verbose_name=_(u"Percent completed"), choices=PERCENTAGES_OPTIONS)

	clg_emission_date = models.DateField(blank=False, null=False, verbose_name=_(u"CLG emission date"))
	price = models.DecimalField(null=True, max_digits=20, decimal_places=2, verbose_name=_(u"Price"))

	# TODO: Add a get_price method that returns the correct price. Either the one in the prototype or
	# the one in the Inventory entry

	def __unicode__(self):
		return u"%s%s%s" % (self.block, self.macro_lot, self.lot)


	def save(self, *args, **kwargs):
		self.unique_id = u"%s%s%s" % (self.block, self.macro_lot, self.lot)

		super(Inventory, self).save(*args, **kwargs)


	class Meta:
		verbose_name = _(u"Realestate")
		verbose_name_plural = _(u"Realestate")


class BridgeCredit(models.Model):
	inventory = models.ForeignKey(Inventory, verbose_name=_(u"Realestate"))
	status = models.CharField(choices=BRIDGE_CREDIT_STATUSES, verbose_name=_(u"Status"), 
		max_length=30, default=0)
	approved_on = models.DateField(blank=False, null=False, verbose_name=_(u"Approved on"))
	approved_amount = models.DecimalField(blank=False, null=False, max_digits=20, 
		decimal_places=2, verbose_name=_(u"Approved amount"))
	ministered_amount = models.DecimalField(blank=False, null=False, max_digits=20, 
		decimal_places=2, verbose_name=_(u"Ministered amount"))


	class Meta:
		verbose_name = _(u"Bridge Credit")
		verbose_name_plural = _(u"Bridge Credits")


class BridgeCreditPayment(models.Model):
	bridge_credit = models.ForeignKey(BridgeCredit, verbose_name=_(u"Bridge credit"))
	amount = models.DecimalField(blank=False, null=False, max_digits=20, 
		decimal_places=2, verbose_name=_(u"Amount"))
	payment_date = models.DateField(blank=False, null=False, verbose_name=_(u"Payment date"))


	class Meta:
		verbose_name = _(u"Bridge Credit Payment")
		verbose_name_plural = _(u"Bridge Credit Payment")


class UtilityType(models.Model):
	name = models.CharField(null=False, blank=False, max_length=50, verbose_name=_(u"Name"))


	class Meta:
		verbose_name = _(u"Utility type")
		verbose_name_plural = _(u"Utility types")


class UtilityPayment(models.Model):
	inventory = models.ForeignKey(Inventory, verbose_name=_(u"Realestate"))
	utility_type = models.ForeignKey(UtilityType, verbose_name=_(u"Utility type"))
	amount = models.DecimalField(blank=False, null=False, max_digits=10, 
		decimal_places=2, verbose_name=_(u"Amount"))
	payment_date = models.DateField(blank=False, null=False, verbose_name=_(u"Payment date"))


	class Meta:
		verbose_name = _(u"Utility payment")
		verbose_name_plural = _(u"Utility payments")