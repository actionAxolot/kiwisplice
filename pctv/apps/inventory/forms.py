from django import forms
from django.forms.widgets import DateInput, TextInput, HiddenInput
from models import (Inventory, Section,
    Prototype, BridgeCredit, BridgeCreditPayment)
from django.forms.models import inlineformset_factory


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        widgets = {
            'construction_end_date': DateInput(format='%d/%m/%Y', attrs={"class": "date-picker"}),
            'clg_emission_date': DateInput(format='%d/%m/%Y', attrs={"class": "date-picker"}),
            'siapa_payment_date': DateInput(format='%d/%m/%Y', attrs={"class": "date-picker"}),
            'predial_payment_date': DateInput(format='%d/%m/%Y', attrs={"class": "date-picker"}),
            'build_end_date': DateInput(format='%d/%m/%Y', attrs={"class": "date-picker"}),
            'unique_id': HiddenInput(),
            'created_by': HiddenInput(),
            'x': HiddenInput(),
            'y': HiddenInput(),
            'user': HiddenInput()
        }


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section


class PrototypeForm(forms.ModelForm):
    class Meta:
        model = Prototype


class BridgeCreditForm(forms.ModelForm):
    class Meta:
        model = BridgeCredit
        widgets = {
            "approved_on": DateInput(format='%d/%m/%Y', attrs={"class": "date-picker"}),
        }


class BridgeCreditPaymentForm(forms.ModelForm):
    class Meta:
        model = BridgeCreditPayment
        widgets = {
            'payment_date': DateInput(format='%d/%m/%Y', attrs={"class": "date-picker"}),
        }


BridgeCreditPaymentsFormset = inlineformset_factory(BridgeCredit, BridgeCreditPayment, form=BridgeCreditPaymentForm, extra=1)
InventoryBridgeCreditFormset = inlineformset_factory(Inventory, BridgeCredit, form=BridgeCreditForm)
