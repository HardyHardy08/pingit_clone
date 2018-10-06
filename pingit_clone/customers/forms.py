# from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Customer


class CustomerCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Customer
        fields = ('username', 'email', 'first_name', 'last_name',
                  'identification_type', 'identification_number', 'contact_number')


class CustomerChangeForm(UserChangeForm):

    class Meta:
        model = Customer
        fields = ('username', 'email')
