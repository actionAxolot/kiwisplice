from django.db import models

# Create your models here.
class ProspectionChannel(models.Model):
	"""How did the people buying this get here?"""
	name = models.CharField(max_length=100)


class ProspectionStatus(models.Model):
	"""
	How is the sale going
	"""
	name = models.CharField(max_length=100)