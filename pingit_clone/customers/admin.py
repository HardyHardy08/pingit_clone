from django.contrib import admin
# from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomerChangeForm, CustomerCreationForm
from .models import Customer


class CustomerAdmin(UserAdmin):
    add_form = CustomerCreationForm
    form = CustomerChangeForm
    model = Customer
    list_display = ['email', 'username', 'contact_number', ]


admin.site.register(Customer, CustomerAdmin)
