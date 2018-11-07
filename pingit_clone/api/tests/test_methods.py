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
