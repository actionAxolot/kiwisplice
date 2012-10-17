from django import forms
from django.forms.models import inlineformset_factory
from models import Prospection, PhoneNumber


class ProspectionForm(forms.ModelForm):
    class Meta:
        model = Prospection


class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber


ProspectionPhoneNumberFormset = inlineformset_factory(Prospection, PhoneNumber, 
    form=PhoneNumberForm, can_delete=False, extra=3, max_num=3)