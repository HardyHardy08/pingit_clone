"""
TODO:
    Customer Model:
    -tests show that Customer can still be saved with empty identification_number field as
    django.db.models' blank=False only apply to form level validation. Add method or something
    in model/manager to overload default save to keep that from passing
    Refactoring:
    - Remove IdentificationType class and use a more django-like method to populate
    identification_type field of Customer
"""
from django.db import models
from model_utils.models import TimeStampedModel

from . import managers


class Merchant(models.Model):
    merchant_ID = models.CharField(max_length=3, blank=False)
    merchant_desc = models.CharField(max_length=50, blank=False)


class AccountType(models.Model):
    account_type_desc = models.CharField(max_length=50, blank=False)


class AccountStatus(models.Model):
    account_status_desc = models.CharField(max_length=20, blank=False)


class Account(models.Model):
    account_status_code = models.ForeignKey(AccountStatus, on_delete=models.PROTECT)
    account_type_code = models.ForeignKey(AccountType, on_delete=models.PROTECT)
    customer_id = models.ForeignKey('customers.Customer', on_delete=models.PROTECT)

    account_number = models.CharField(max_length=15, primary_key=True, blank=False)
    current_balance = models.FloatField(default=0.0)
    other_details = models.CharField(max_length=200, blank=True)

    objects = managers.AccountManager()


class TransactionType(models.Model):
    transaction_type_desc = models.CharField(max_length=50, blank=False)


class Transaction(TimeStampedModel):
    account_number = models.ForeignKey(Account, on_delete=models.PROTECT)
    merchant_ID = models.ForeignKey(Merchant, on_delete=models.PROTECT)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.PROTECT)

    transaction_amount = models.FloatField(default=0.0, blank=False)
    other_details = models.CharField(max_length=140)

    objects = managers.TransactionManager()
