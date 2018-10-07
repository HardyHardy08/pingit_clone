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
    merchant_ID = models.IntegerField(primary_key=True, blank=False)
    merchant_desc = models.CharField(max_length=50, blank=False)


class Transaction(TimeStampedModel):
    account_number = models.ForeignKey()
    merchant_ID = models.ForeignKey()
    transaction_type = models.ForeignKey()

    transaction_amount = models.FloatField(default=0.0, blank=False)
    other_details = models.CharField(max_length=140)

    objects = managers.TransactionManager


class TransactionType(models.Model):
    transaction_type_desc = models.CharField(max_length=50, blank=False)


class Account(models.Model):
    account_status_code = models.ForeignKey()
    account_type_code = models.ForeignKey()
    customer_id = models.ForeignKey

    account_number = models.CharField(max_length=15, primary_key=True, blank=False)
    current_balance = models.FloatField(default=0.0)
    other_details = models.CharField(max_length=200, blank=True)

    objects = managers.TransactionManager


class AccountType(models.Model):
    account_type_desc = models.CharField(max_length=50, blank=False)
