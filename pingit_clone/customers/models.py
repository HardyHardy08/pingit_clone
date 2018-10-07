"""
TODO:
    Customer Model:
    -tests show that Customer can still be saved with empty identification_number field as
    django.db.models' blank=False only apply to form level validation. Add method or something
    in model/manager to overload default save to keep that from passing
    Refactoring:
    - Remove IdentificationType class and use a more django-like method to populate
    identification_type field of Customer
"""

from django.contrib.auth.models import AbstractUser
from django.db import models

from . import managers


class IdentificationType(models.Model):
    identification_description = models.CharField(max_length=50, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.identification_description


class Customer(AbstractUser):
    identification_type = models.ForeignKey(IdentificationType, on_delete=models.PROTECT)
    identification_number = models.CharField(max_length=20, blank=False)
    contact_number = models.CharField(max_length=15, blank=False)

    objects = managers.CustomerManager()

    def __str__(self):
        return self.email + ": " + self.first_name + " " + self.last_name
