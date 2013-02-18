# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, unique=True)
    commission_percentage = models.DecimalField(max_digits=5, decimal_places=2,
                                                verbose_name=u"Porcentaje de comisión", default=10)
