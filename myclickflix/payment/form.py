from django import forms
from .models import Order


class RechargeForm(forms.Form):
    code = forms.CharField(label="Recharge Code", max_length=50)
