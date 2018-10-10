import json, random
from collections import namedtuple
from django.db import models


class TransactionManager(models.Manager):

    def transaction_type(self, transaction_type):
        from .models import TransactionType
        return TransactionType.objects.get(transaction_type_desc=transaction_type)

    def create_transfer_transaction(self, account_number, merchant_ID, transaction_type,
                                    transaction_amount, other_details, destination_number):
        source = self.model(
            account_number=account_number,
            merchant_ID=merchant_ID,
            transaction_type=self.transaction_type("Transfer"),
            transaction_amount=transaction_amount,
            other_details=json.dumps(
                {'msg': other_details, 'destination': destination_number.account_number}))
        source.save()
        destination = self.model(
            account_number=account_number,
            merchant_ID=merchant_ID,
            transaction_type=self.transaction_type("Deposit"),
            transaction_amount=transaction_amount,
            other_details=json.dumps(
                {'msg': other_details, 'source': account_number.account_number}))
        destination.save()
        return namedtuple('transfer', ['source', 'destination'])(source, destination)


class AccountManager(models.Manager):

    def account_type_code(self, account_type):
        from .models import AccountType
        return AccountType.objects.get(account_type_desc=account_type)

    def account_status_code(self, account_status):
        from .models import AccountStatus
        return AccountStatus.objects.get(account_status_desc=account_status)

    def _account_number_generator(self):
        return "001-" + str(random.random() * 100000)[:5]

    def create_account(self, account_type_code, customer, starting_balance, other_details=''):
        new_account = self.model(
            account_status_code=self.account_status_code("Active"),
            account_type_code=self.account_type_code(account_type_code),
            customer_id=customer,
            account_number=self._account_number_generator(),
            current_balance=starting_balance,
            other_details=other_details
        )
        new_account.save()
        return new_account
