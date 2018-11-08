import json
from rest_framework import status
from banking.models import Account
from banking.serializers import AccountSerializer
from customers.models import Customer
from rest_framework.test import APITestCase
from django.urls import reverse


class AccountDetailTests(APITestCase):
    fixtures = ['bank_fixtures']

    def setUp(self):
        self.valid_account = Account.objects.latest()
        self.valid_user = {
            "username": "rahmaratnasyani",
            "password": "123123qweqwe"
        }
        self.not_owned_account = Account.objects.earliest()

    def test_successful_valid_get_account(self):
        self.client.login(**self.valid_user)
        response = self.client.get(
            reverse('api:account-detail',
                    kwargs={'account_number': self.valid_account.account_number})
        )
        serializer = AccountSerializer(
            Account.objects.get(account_number=self.valid_account.account_number),
        )
        self.assertEqual(json.loads(response.content), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_successful_invalid_get_account_return_404(self):
        self.client.login(**self.valid_user)
        response = self.client.get(
            reverse('api:account-detail',
                    kwargs={'account_number': 'asdasdasd'})
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_unauthorized_account_detail_request_return_403(self):
        response = self.client.get(
            reverse('api:account-detail',
                    kwargs={'account_number': self.valid_account.account_number})
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_account_detail_request_on_not_owned_account_return_404(self):
        """
        This should make more sense to return 403, but the view's get_queryset() already filters
        the queryset to the requesting user, thus returning 404 instead.
        """
        self.client.login(**self.valid_user)
        response = self.client.get(
            reverse('api:account-detail',
                    kwargs={'account_number': self.not_owned_account.account_number})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class AccountListTests(APITestCase):
    fixtures = ['bank_fixtures']

    def setUp(self):
        self.valid_user = {
            "username": "rahmaratnasyani",
            "password": "123123qweqwe"
        }

    def test_valid_account_list_request(self):
        self.client.login(**self.valid_user)
        response = self.client.get(reverse('api:account-list'))
        serializer = AccountSerializer(
            Account.objects.filter(
                customer_id=Customer.objects.get(username=self.valid_user['username'])),
            many=True
        )
        self.assertEqual(json.loads(response.content), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TransactionCreateTests(APITestCase):
    fixtures = ['bank_fixtures']

    def test_transaction_api_create_valid_request(self):
        self.fail('create test!')

    def test_transaction_api_fail_bad_request(self):
        self.fail('create test!')

    def test_transaction_api_create_on_authorized_requester(self):
        self.fail('create test!')

    def test_transaction_api_reject_unauthorized_requesters(self):
        self.fail('create test!')
