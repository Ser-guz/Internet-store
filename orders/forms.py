from django import forms
from .models import *


class CheckoutContactForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(max_length=16, required=True)
