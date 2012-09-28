# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
import datetime

# Porcentajes options... this is probably retardedr
PERCENTAGES_OPTIONS = tuple([(x, unicode(x) + u"%") for x in xrange(0, 110, 10)])


# How's the brige credit going?
BRIDGE_CREDIT_STATUSES = (
    (u"Liberado", _(u"Liberado")),
    (u"No liberado", _(u"No Liberado")),
)


# Construction options
CONSTRUCTION_STATUS = (
    (u"En obra", _(u"En obra")),
    (u"Libre", _(u"Libre")),
    (u"Bloqueado", _(u"Bloqueado")),
    (u"Con cliente", _(u"Con cliente")),
    (u"Firmado", _(u"Firmado")),
)


class Prototype(models.Model):
    name = models.CharField(blank=False, null=False, max_length=50, verbose_name=_(u'Name'))
    image = models.ImageField(upload_to="prototype_pics", null=True, blank=True, verbose_name=_(u"Image"))
    price = models.CharField(blank=False, null=False, max_length=50, verbose_name=_(u"Price"))

    def __unicode__(self):
        return u"%s" % self.name

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
    created_by = models.ForeignKey(User, verbose_name=_(u'Created by'), blank=True, null=True)
    prototype = models.ForeignKey(Prototype, verbose_name=_(u'Prototype'))
    section = models.ForeignKey(Section, verbose_name=_(u"Section"))
    construction_status = models.CharField(max_length=40, blank=False, null=False,
        choices=CONSTRUCTION_STATUS, verbose_name=_(u"Construction status"))
    # location_status = models.CharField(blank=False, null=False,
        # max_length=50, verbose_name=_(u"Location Status"), choices=LOCATION_STATUS)
    cuv = models.CharField(max_length=200, blank=True, null=False, verbose_name=_(u'CUV'), )
    official_id = models.CharField(max_length=200, blank=False, null=False, verbose_name=_(u"Official Identifier"))

    # TODO: This one should be filled automatically
    unique_id = models.CharField(max_length=50, blank=True, null=True,
        verbose_name=_(u"Identificador único"))
    block = models.CharField(max_length=50, blank=False, null=False, verbose_name=_(u'Block'))
    macro_lot = models.CharField(blank=False, null=False,
        verbose_name=_(u'Macro lot'), max_length=50)
    lot = models.CharField(blank=False, null=False,
        verbose_name=_(u'Lot'), max_length=50)
    street = models.CharField(blank=False, null=False,
        verbose_name=_(u"Street"), max_length=50)
    number = models.CharField(blank=False, null=False,
        verbose_name=_(u'Realestate number'), max_length=50)
    lot_size = models.IntegerField(blank=False, null=False, verbose_name=_(u"Extensión de terreno"))
    construction_size = models.IntegerField(blank=False, null=False, verbose_name=_(u'Extensión de construcción'))
    construction_end_date = models.DateField(blank=False, null=False, verbose_name=_(u"Construction end date"))

    build_end_date = models.DateField(blank=True, null=True, verbose_name=_(u"Fecha de terminación de obra"))
    percent_completed = models.IntegerField(blank=False, null=False,
        default=0, verbose_name=_(u"Percent completed"), choices=PERCENTAGES_OPTIONS)

    # New additions about SIAPA, PREDIAL and CLG
    siapa_account = models.CharField(blank=False, null=False, max_length=50, verbose_name=_(u"Cuenta SIAPA"))
    predial_account = models.CharField(blank=False, null=False, max_length=50, verbose_name=_(u"Cuenta PREDIAL"))
    clg_folium = models.CharField(blank=False, null=False, max_length=50, verbose_name=_(u"Folio CLG"))

    # When was stuff payed?
    siapa_payment_date = models.DateField(blank=True, null=True, verbose_name=_(u"Fecha de pago SIAPA"))
    predial_payment_date = models.DateField(blank=True, null=True, verbose_name=_(u"Fecha de pago PREDIAL"))
    clg_emission_date = models.DateField(blank=False, null=False, verbose_name=_(u"CLG emission date"))
    price = models.DecimalField(null=True, blank=True, max_digits=20, decimal_places=2, verbose_name=_(u"Price"))
    x = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=6)
    y = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=6)

    # TODO: Add a get_price method that returns the correct price. Either the one in the prototype or
    # the one in the Inventory entry

    def __unicode__(self):
        return u"%s" % self.cuv

    def save(self, *args, **kwargs):
        """
        Prepopulate the CUV field. Every element of it must be 2 characters long. If
        they're not just append a 0
        """
        self.block = self.block if len(self.block) > 1 else "0%s" % self.block
        self.macro_lot = self.macro_lot if len(self.macro_lot) > 1 else "0%s" % self.macro_lot
        self.lot = self.lot if len(self.lot) > 1 else "0%s" % self.lot
        self.unique_id = u"%s%s%s" % (self.block, self.macro_lot, self.lot)
        self.price = self.price if self.price else self.get_price()

        super(Inventory, self).save(*args, **kwargs)

    def get_price(self):
        """
        Returns the price of the inventory item if it's defined. Otherwise it
        returns the Prototype's defined price
        """
        return self.price if self.price else self.prototype.price

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
    payed_amount = models.DecimalField(blank=True, null=False, max_digits=20,
        decimal_places=2, verbose_name=_(u"Cantidad pagada"))

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
