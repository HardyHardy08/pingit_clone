from django.core.validators import MinValueValidator
from django.db import models
from model_utils.models import TimeStampedModel

from . import managers


class Merchant(models.Model):
    merchant_ID = models.CharField(max_length=3, blank=False, unique=True)
    merchant_desc = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.merchant_ID + " : " + self.merchant_desc


class AccountType(models.Model):
    account_type_desc = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.account_type_desc


class AccountStatus(models.Model):
    account_status_desc = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.account_status_desc


class Account(TimeStampedModel):
    account_status_code = models.ForeignKey(AccountStatus, on_delete=models.PROTECT)
    account_type_code = models.ForeignKey(AccountType, on_delete=models.PROTECT)
    customer_id = models.ForeignKey('customers.Customer', on_delete=models.PROTECT)

    account_number = models.CharField(max_length=15, primary_key=True, blank=False)
    current_balance = models.DecimalField(max_digits=20, decimal_places=2,
                                          default=0.0, blank=False)
    other_details = models.CharField(max_length=200, blank=True)

    objects = managers.AccountManager()

    def _calculate_current_balance(self):
        queryset = self.transaction_set.filter(created__gte=self.modified).values(
            'transaction_amount', 'transaction_type')
        transfer_transaction, deposit_transaction = 1, 2
        outgoing, incoming = 0, 0
        for transaction in queryset:
            if transaction['transaction_type'] == transfer_transaction:
                outgoing += transaction['transaction_amount']
            if transaction['transaction_type'] == deposit_transaction:
                incoming += transaction['transaction_amount']
        return self.current_balance - outgoing + incoming

    def _update_balance(self):
        self.current_balance = self._calculate_current_balance()
        self.save()

    def __str__(self):
        return self.account_number

    class Meta:
        get_latest_by = 'created'


class TransactionType(models.Model):
    transaction_type_desc = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.transaction_type_desc


class Transaction(TimeStampedModel):
    account_number = models.ForeignKey(Account, on_delete=models.PROTECT)
    merchant_ID = models.ForeignKey(Merchant, on_delete=models.PROTECT)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.PROTECT)

    transaction_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=False,
                                             validators=[MinValueValidator(0.00)])
    other_details = models.CharField(max_length=140)

    objects = managers.TransactionManager()

    def __str__(self):
        return (self.account_number.account_number +
                " : " + self.transaction_type.transaction_type_desc)

    class Meta:
        get_latest_by = 'created'
        ordering = ['-created']
