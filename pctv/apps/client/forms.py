from django.forms.models import ModelForm
from django.forms.models import inlineformset_factory
from django.forms.widgets import HiddenInput, DateInput
from models import Client
from apps.payment.models import Payment


class ClientForm(ModelForm):
    class Meta:
        model = Client
        widgets = {
            'prospection': HiddenInput(),
            'integration_date': DateInput(format='%d/%m/%Y', attrs={"class": "date-picker"}),
            'signature_date': DateInput(format='%d/%m/%Y', attrs={"class": "date-picker"}),
            'auth_date': DateInput(format='%d/%m/%Y', attrs={"class": "date-picker"}),
            'pricing_date': DateInput(format='%d/%m/%Y', attrs={"class": "date-picker"}),
            'payment_date': DateInput(format='%d/%m/%Y', attrs={"class": "date-picker"}),
            'delivery_date': DateInput(format='%d/%m/%Y', attrs={"class": "date-picker"}),
        }


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        widgets = {
            'date_due': DateInput(format='%d/%m/%Y', attrs={"class": "date-picker"}),
        }
        fields = ("amount", "date_due")


class PaymentCollectForm(ModelForm):
    class Meta:
        model = Payment
        widgets = {
            'date_payed': DateInput(format='%d/%m/%Y', attrs={"class": "date-picker"}),
        }
        exclude = ("amount", "date_due")


ClientPaymentFormSet = inlineformset_factory(Client, Payment, form=PaymentForm,
                                             extra=10, can_delete=False)

ClientPaymentCollectFormSet = inlineformset_factory(Client, Payment,
                                                    form=PaymentCollectForm,
                                                    extra=10, can_delete=False)
