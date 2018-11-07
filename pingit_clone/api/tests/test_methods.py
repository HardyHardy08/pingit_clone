import json
from rest_framework import status
from banking.models import Account
from banking.serializers import AccountSerializer
from rest_framework.test import APITestCase, APIRequestFactory
from django.urls import reverse


class AccountDetailTests(APITestCase):

    # def setUp(self):

    def test_successful_valid_get_account(self):
        response = self.client.get(
            reverse('snippet-detail',
                    kwargs={'pk': self.authorized_user_snippet.pk})
        )
        request = APIRequestFactory().get(
            reverse('snippet-detail',
                    kwargs={'pk': self.authorized_user_snippet.pk})
        )
        serializer = AccountSerializer(
            Account.objects.get(pk=self.authorized_user_snippet.pk),
            context={'request': request}
        )
        self.assertEqual(json.loads(response.content), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
