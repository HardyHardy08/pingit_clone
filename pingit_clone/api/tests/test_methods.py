import json
from rest_framework import status
from banking.models import Account
from banking.serializers import AccountSerializer
from rest_framework.test import APITestCase
from django.urls import reverse


class AccountDetailTests(APITestCase):
    fixtures = ['bank_fixtures']

    def setUp(self):
        self.valid_account = Account.objects.latest()

    def test_successful_valid_get_account(self):
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
        response = self.client.get(
            reverse('api:account-detail',
                    kwargs={'account_number': 'asdasdasd'})
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


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
