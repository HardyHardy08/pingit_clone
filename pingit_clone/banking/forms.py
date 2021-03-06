# from django import forms
from django import forms
from .models import Account, Transaction, TransactionType


class AccountCreationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['account_type_code']
        labels = {'account_type_code': 'Account Type'}


class TransactionCreationForm(forms.ModelForm):
    destination_number = forms.ModelChoiceField(
        queryset=Account.objects.all())
    transaction_amount = forms.DecimalField(min_value=0)
    transaction_type = forms.ModelChoiceField(
        queryset=TransactionType.objects.exclude(transaction_type_desc="Deposit"))

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['account_number'].queryset = Account.objects.filter(customer_id=user)

    class Meta:
        model = Transaction
        fields = ['account_number', 'merchant_ID', 'transaction_type', 'transaction_amount',
                  'other_details', 'destination_number']
