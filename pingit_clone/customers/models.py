from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
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

    REQUIRED_FIELDS = [
        'email', 'first_name', 'last_name', 'identification_type',
        'identification_number', 'contact_number'
    ]

    def save(self, *args, **kwargs):
        if not self.identification_number:
            raise ValidationError("Identication Number cannot be empty.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email + ": " + self.first_name + " " + self.last_name
