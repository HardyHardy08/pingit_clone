# from django import forms
from django.forms import ModelForm
from .models import Account


class AccountCreationForm(ModelForm):
    class Meta:
        model = Account
        fields = ['account_type_code']
        labels = {'account_type_code': 'Account Type'}
