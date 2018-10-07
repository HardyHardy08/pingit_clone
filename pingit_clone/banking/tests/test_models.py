from django.core.exceptions import ValidationError
from django.test import TestCase
from banking.models import (
    Transaction, TransactionType, Account, AccountStatus, AccountType, Merchant
)
from customers.models import Customer
from customers.tests.test_models import valid_customer_data, setup_IdentificationTypes


def valid_account():
    return {
        'account_status_code': AccountStatus.objects.get(account_status_desc='Active'),
        'account_type_code': AccountType.objects.get(account_type_desc="Savings"),
        'customer_id': Customer.objects.get(username='JohnDoe'),
        'account_number': '123-123-123000',
        'current_balance': '1000.0',
        'other_details': '',
    }


def create_fixtures():
    # Customer app models
    setup_IdentificationTypes()
    Customer.objects.create(**valid_customer_data())

    TransactionType.objects.create(transaction_type_desc="Transfer")
    AccountStatus.objects.create(account_status_desc="Active")
    AccountType.objects.create(account_type_desc="Savings")
    Merchant.objects.create(merchant_ID="001", merchant_desc="Boong Bank")


class DefaultTransactionTest(TestCase):
    """
    Test default model manager functions for transaction model
    """

    def setUp(self):
        create_fixtures()
        account = Account.objects.create(**valid_account())
        self.valid_transaction = {
            'account_number': account,
            'merchant_ID': Merchant.objects.get(merchant_ID="001"),
            'transaction_type': TransactionType.objects.get(transaction_type_desc="Transfer"),
            'transaction_amount': 10.0,
            'other_details': 'August/18 rent',
        }
        self.invalid_transaction = {
            'account_number': account,
            'merchant_ID': Merchant.objects.get(merchant_ID="001"),
            'transaction_type': TransactionType.objects.get(transaction_type_desc="Transfer"),
            'transaction_amount': 'tree fiddy',
            'other_details': 'August/18 rent',
        }

    def test_valid_create_transaction(self):
        new_transaction = Transaction.objects.create(**self.valid_transaction)
        self.assertIsInstance(new_transaction, Transaction)

    def test_invalid_create_transaction(self):
        with self.assertRaises(ValueError):
            Transaction.objects.create(**self.invalid_transaction)

    def test_valid_update_transaction(self):
        transaction = Transaction.objects.create(**self.valid_transaction)
        new_merchant = Merchant.objects.create(merchant_ID="002",
                                               merchant_desc="Zonk Bank")
        transaction.merchant_ID = new_merchant
        transaction.save()
        self.assertEqual(
            Transaction.objects.get(merchant_ID=new_merchant),
            transaction)

    def test_invalid_update_transaction(self):
        transaction = Transaction.objects.create(**self.valid_transaction)
        transaction.transaction_amount = "one hundred"
        with self.assertRaises(ValueError):
            transaction.save()

    def test_delete_transaction(self):
        transaction = Transaction.objects.create(**self.valid_transaction)
        transaction.delete()
        with self.assertRaises(Transaction.DoesNotExist):
            Transaction.objects.get(pk=transaction.pk)


# class CustomTransactionTest(unittest):
    """
    Test custom model manager functions for transaction model
    """


class DefaultAccountTest(TestCase):
    """
    Test default model manager functions for account model
    """

    def setUp(self):
        create_fixtures()
        self.valid_account = valid_account()
        self.invalid_account = {
            'account_status_code': AccountStatus.objects.get(account_status_desc='Active'),
            'account_type_code': AccountType.objects.get(account_type_desc="Savings"),
            'customer_id': '',
            'account_number': '123-123-123000',
            'current_balance': 200,
            'other_details': '',
        }

    def test_valid_create_account(self):
        new_account = Account.objects.create(**self.valid_account)
        self.assertIsInstance(new_account, Account)

    def test_invalid_create_account(self):
        with self.assertRaises(ValueError):
            Account.objects.create(**self.invalid_account)

    def test_valid_update_account(self):
        account = Account.objects.create(**self.valid_account)
        account.current_balance = 50.0
        account.save()
        self.assertEqual(account.current_balance, 50.0)

    def test_invalid_update_account(self):
        account = Account.objects.create(**self.valid_account)
        account.current_balance = "two hundred"
        with self.assertRaises(ValueError):
            account.save()

    def test_delete_account(self):
        account = Account.objects.create(**self.valid_account)
        account.delete()
        with self.assertRaises(Account.DoesNotExist):
            Account.objects.get(pk=account.pk)

# class CustomAccountTest(unittest):
    """
    Test custom model manager functions for account model
    """
