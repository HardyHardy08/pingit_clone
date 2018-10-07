from django.core.exceptions import ValidationError
from django.test import TestCase
from customers.models import Customer, IdentificationType


class DefaultCustomerTest(TestCase):
    """
    Test default model manager functions for customer model
    """

    def setUp(self):
        IdentificationType.objects.create(identification_description="KTP")
        IdentificationType.objects.create(identification_description="SIM")
        IdentificationType.objects.create(identification_description="Paspor")

        self.valid_data = {
            'username': 'JohnDoe',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@boongbank.com',
            'contact_number': '08123123123',
            'password': '123123123123',
            'identification_type': IdentificationType.objects.get(
                identification_description="KTP"),
            'identification_number': '0123456789QWERTY'
        }
        self.invalid_data = {
            'username': 'JackDoe',
            'first_name': 'Jack',
            'last_name': 'Doe',
            'email': 'thisisnotanemail',
            'contact_number': '081321321321',
            'password': '123123123123',
            'identification_type': '',
            'identification_number': ''
        }

    def test_valid_create_customer(self):
        new_customer = Customer.objects.create_user(**self.valid_data)
        self.assertIsInstance(new_customer, Customer)

    def test_invalid_create_customer(self):
        # Not sure how to write down this test
        with self.assertRaises(ValueError):
            Customer.objects.create_user(**self.invalid_data)

    def test_valid_update_customer(self):
        new_customer = Customer.objects.create_user(**self.valid_data)
        new_customer.first_name = "notWhatItWas"
        new_customer.save()
        self.assertEqual(new_customer.first_name, "notWhatItWas")

    def test_invalid_update_customer(self):
        # Not sure how to write down this test
        new_customer = Customer.objects.create_user(**self.valid_data)
        new_customer.identification_number = ''
        with self.assertRaises(ValidationError):  # Should be ValueError or something
            new_customer.save()                         # error saying it should not be blank

    def test_delete_customer(self):
        new_customer = Customer.objects.create_user(**self.valid_data)
        new_customer.delete()
        with self.assertRaises(Customer.DoesNotExist):
            Customer.objects.get(username=self.valid_data['username'])

# class CustomCustomerTest(unittest):
    """
    Test custom model manager functions for customer model
    """
