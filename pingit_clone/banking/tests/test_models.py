from django.core.exceptions import ValidationError
from django.test import TestCase
from banking.models import Transaction, Account


class DefaultTransactionTest(TestCase):
    """
    Test default model manager functions for transaction model
    """

    def setUp(self):
        self.valid_transaction = {}
        self.invalid_transaction = {}

    def test_valid_create_transaction(self):
        new_transaction = Transaction.objects.create(**self.valid_transaction)
        self.assertIsInstance(new_transaction, Transaction)

    def test_invalid_create_transaction(self):
        with self.assertRaises(ValidationError):
            Transaction.objects.create(**self.invalid_transaction)

    def test_valid_update_transaction(self):
        transaction = Transaction.objects.create(**self.valid_transaction)
        transaction.merchant_ID = "5"
        transaction.save()
        self.assertEqual(transaction.merchant_ID, "5")

    def test_invalid_update_transaction(self):
        transaction = Transaction.objects.create(**self.valid_transaction)
        transaction.amount = 0
        with self.assertRaises(ValidationError):
            Transaction.save()

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
        self.valid_account = {}
        self.invalid_account = {}

    def test_valid_create_account(self):
        new_account = Account.objects.create(**self.valid_account)
        self.assertIsInstance(new_account, Account)

    def test_invalid_create_account(self):
        with self.assertRaises(ValidationError):
            Account.objects.create(**self.invalid_account)

    def test_valid_update_account(self):
        account = Account.objects.create(**self.valid_account)
        account.current_balance = 50.0
        account.save()
        self.assertEqual(account.current_balance, 50.0)

    def test_invalid_update_account(self):
        account = Account.objects.create(**self.valid_account)
        account.amount = 200
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
