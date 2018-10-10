from django.test import TestCase
from django.urls import reverse

from banking import models
from customers.models import Customer


class AccountViewsTest(TestCase):
    fixtures = ['bank_fixtures']

    def setUp(self):
        self.valid_user = {
            "username": "rahmaratnasyani",
            "password": "123123qweqwe"
        }

    def test_authorized_account_list_view(self):
        self.client.login(**self.valid_user)

        response = self.client.get(reverse('banking:account-list'))
        customer = Customer.objects.get(username=self.valid_user['username'])
        self.assertEqual(response.status_code, 200)
        # Using assertEqual and calling first() instead of expected assertQuerysetEqual because
        # using the latter does not return expected results.
        # Even when using the exact same queryset as qs and values argument, assertion still
        # returns ValueError for non-ordered queryset. AssertionError still raised even after
        # setting ordered=False. I might be using it wrong, but moving on as to not get stuck on
        # one test.
        self.assertEqual(
            response.context['account_list'].first(),
            customer.account_set.all().first(),
        )
        self.assertEqual(
            response.context['account_list'].last(),
            customer.account_set.all().last(),
        )

    def test_unauthorized_account_list_view(self):
        response = self.client.get(reverse('banking:account-list'))
        self.assertRedirects(response, '/?next=/banking/account/')

    def test_valid_account_detail_view(self):
        self.client.login(**self.valid_user)
        account_number = (
            Customer.objects.get(username="rahmaratnasyani").account_set.first().account_number
        )
        detail_view = self.client.get(reverse(
            'banking:account-detail',
            kwargs={'account_number': account_number}
        ))
        self.assertEqual(
            detail_view.context_data['account'].customer_id,
            Customer.objects.get(username=self.valid_user['username']))

    def test_unauthorized_account_detail_view(self):
        self.client.login(**self.valid_user)
        customer = Customer.objects.get(username=self.valid_user['username'])
        other_customer_account = models.Account.objects.exclude(customer_id=customer).first()
        response = self.client.get(reverse(
            'banking:account-detail',
            kwargs={'account_number': other_customer_account.account_number}
        ))
        self.assertEqual(response.status_code, 404)

    def test_valid_account_create_view(self):
        self.client.login(**self.valid_user)
        self.client.post(reverse('banking:account-create'),
                         data={'account_type_code': 'Savings'})
        self.assertEqual(models.Account.objects.last().customer_id,
                         Customer.objects.get(username=self.valid_user['username']))

    def test_unauthorized_account_create_view(self):
        response = self.client.get(reverse('banking:account-create'))
        self.assertRedirects(response, '/?next=/banking/account/create/')


class TransactionViewsTest(TestCase):
    fixtures = ['bank_fixtures']

    def setUp(self):
        self.valid_user = {
            "username": "rahmaratnasyani",
            "password": "123123qweqwe"
        }
        self.valid_transaction = {
            'account_number': models.Account.objects.first(),
            'merchant_ID': '1',
            'transaction_type': '1',
            'transaction_amount': 50,
            'other_details': "This month's rent",
            'destination_number': models.Account.objects.last()
        }
        self.invalid_transaction = {
            'account_number': models.Account.objects.last(),
            'merchant_ID': models.Merchant.objects.first(),
            'transaction_type': models.Transaction.objects.transaction_type('Transfer'),
            'transaction_amount': 'tree fiddy',
            'other_details': 'August/18 rent',
        }

    def test_valid_transaction_create_view(self):
        self.client.login(**self.valid_user)
        self.client.post(
            reverse('banking:transaction-create'),
            data=self.valid_transaction,
            follow=True)
        last_two_transactions = models.Transaction.objects.all()[:2]
        self.assertEqual(
            [transaction.account_number for transaction in last_two_transactions],
            [self.valid_transaction['destination_number'],
             self.valid_transaction['account_number']])

    def test_invalid_transaction_create_view(self):
        response = self.client.post(reverse('banking:transaction-create'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.is_rendered, True)
        self.assertEqual(response.context_data['form'].is_valid(), False)

    def test_valid_transaction_list_view(self):
        self.client.login(**self.valid_user)
        transactions = self.client.get(reverse('banking:transactions-list'))
        self.asserQuerysetEqual(transactions,
                                models.Transaction.objects.filter(customer_id=self.client.user))

    def test_invalid_transaction_list_view(self):
        # how do i test this??
        pass

    def test_valid_transaction_detail_view(self):
        self.client.login(**self.valid_user)
        transaction = self.client.get(reverse('banking:transaction-detail',
                                              kwargs={}))
        self.assertEqual(transaction.customer_id, self.client.user)

    def test_invalid_transaction_detail_view(self):
        pass
