from django.db import models

# Create your models here.
class FinancialChannel(models.Model):
	"""Hold financial channel information and whatnot"""
	name = models.CharField(max_length=100, null=False, blank=False)