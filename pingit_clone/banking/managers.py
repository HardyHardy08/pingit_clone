import random

from django.db import models


class TransactionManager(models.Manager):
    pass


class AccountManager(models.Manager):

    def account_type_code(self, account_type):
        from .models import AccountType
        return AccountType.objects.get(account_type_desc=account_type)

    def account_status_code(self, account_status):
        from .models import AccountStatus
        return AccountStatus.objects.get(account_status_desc=account_status)

    def _account_number_generator(self):
        return "001-" + str(random.random() * 100000)[:5]

    def create_savings_account(self, customer, starting_balance, other_details=''):
        new_savings_account = self.model(
            account_status_code=self.account_status_code("Active"),
            account_type_code=self.account_type_code("Savings"),
            customer_id=customer,
            account_number=self._account_number_generator(),
            current_balance=starting_balance,
            other_details=other_details
        )
        new_savings_account.save()
        return new_savings_account

    def create_deposit_account(self, customer, starting_balance, other_details=''):
        new_deposit_account = self.model(
            account_status_code=self.account_status_code("Active"),
            account_type_code=self.account_type_code("Deposit"),
            customer_id=customer,
            account_number=self._account_number_generator(),
            current_balance=starting_balance,
            other_details=other_details
        )
        new_deposit_account.save()
        return new_deposit_account
