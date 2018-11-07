from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    account_type_code = serializers.StringRelatedField()

    class Meta:
        model = Account
        fields = ('account_type_code', 'account_number', 'current_balance')
        read_only_fields = ('account_type_code', 'account_number', 'current_balance')
