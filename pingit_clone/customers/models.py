from django.contrib.auth.models import AbstractUser
from django.db import models


class IdentificationType(models.Model):
    identification_description = models.CharField(max_length=50, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.identification_description


class Customer(AbstractUser):
    identification_type = models.ForeignKey(IdentificationType, on_delete=models.PROTECT)
    identification_number = models.CharField(max_length=20, blank=False)
    contact_number = models.CharField(max_length=15, blank=False)

    def __str__(self):
        return self.email + ": " + self.first_name + " " + self.last_name
