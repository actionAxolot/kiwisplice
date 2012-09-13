from django import forms
from django.forms.widgets import DateInput, TextInput, HiddenInput
from models import Inventory


class InventoryForm(forms.ModelForm):
	class Meta:
		model = Inventory
		widgets = {
			'construction_end_date': DateInput(format='%d/%m/%Y', attrs={"class": "date-picker"}),
			'clg_emission_date': DateInput(format='%d/%m/%Y', attrs={"class": "date-picker"}),
			'cuv': TextInput(attrs={"disabled": "disabled"}),
			'created_by': HiddenInput(),
		}


	def __init__(self, *args, **kwargs):
		self._user = kwargs.pop("user")
		super(InventoryForm, self).__init__(*args, **kwargs)


	def save(self, commit=True):
		inst = super(InventoryForm, self).save(commit=False)
		inst.created_by = self._user
		if commit:
			inst.save()
		return inst