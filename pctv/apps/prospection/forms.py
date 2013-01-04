from django import forms
from django.forms.models import inlineformset_factory
from models import Prospection, PhoneNumber
import datetime

MONTHS = (
    (1, "Enero"),
    (2, "Febrero"),
    (3, "Marzo"),
    (4, "Abril"),
    (5, "Mayo"),
    (6, "Junio"),
    (7, "Julio"),
    (8, "Agosto"),
    (9, "Septiembre"),
    (10, "Octubre"),
    (11, "Noviembre"),
    (12, "Diciembre"), 
)

YEARS = ((c, c) for c in xrange(2000, datetime.date.today().year + 1))

class ProspectionForm(forms.ModelForm):
    class Meta:
        model = Prospection

class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        
        
class FilterForm(forms.Form):
    # Just add filters and shit
    month = forms.IntegerField(initial=datetime.date.today().month, widget=forms.Select(choices=MONTHS))
    year = forms.IntegerField(initial=datetime.date.today().year, widget=forms.Select(choices=YEARS))


ProspectionPhoneNumberFormset = inlineformset_factory(Prospection, PhoneNumber, 
    form=PhoneNumberForm, can_delete=False, extra=3, max_num=3)