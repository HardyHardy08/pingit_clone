from rest_framework import serializers
from .models import Account, Transaction


class AccountSerializer(serializers.ModelSerializer):
    account_type_code = serializers.StringRelatedField()

    class Meta:
        model = Account
        fields = ('account_type_code', 'account_number', 'current_balance')
        read_only_fields = ('account_type_code', 'account_number', 'current_balance')


class TransactionSerializer(serializers.ModelSerializer):
    destination_number = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all())

    def save(self):
        return Transaction.objects.create_transfer_transaction(**self.validated_data)

    class Meta:
        model = Transaction
        fields = ('account_number', 'merchant_ID', 'transaction_type',
                  'transaction_amount', 'other_details', 'destination_number')
