from rest_framework import generics
from banking.serializers import AccountSerializer
from banking.models import Account


class AccountDetail(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'account_number'
