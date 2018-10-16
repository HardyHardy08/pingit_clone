from django.contrib import auth
from django.test import TestCase
from django.urls import reverse

from .test_models import valid_customer_data, setup_IdentificationTypes


class CustomerViewsTest(TestCase):

    def setUp(self):
        setup_IdentificationTypes()

    def test_after_successful_signup_redirect_to_home_page_and_login(self):
        data = valid_customer_data()
        data['identification_type'] = data['identification_type'].pk
        data['password1'] = "123qwerty098"
        data['password2'] = "123qwerty098"

        response = self.client.post(reverse('customers:signup'), data=data)

        user = auth.get_user(self.client)
        self.assertRedirects(response, '/')
        assert user.is_authenticated
