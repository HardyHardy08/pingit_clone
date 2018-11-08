from rest_framework import generics, permissions
from banking.serializers import AccountSerializer
from banking.models import Account
from .permissions import IsOwner


class AccountDetail(generics.RetrieveAPIView):
    serializer_class = AccountSerializer
    lookup_field = 'account_number'
    permission_classes = (permissions.IsAuthenticated, IsOwner,)

    def get_queryset(self):
        return Account.objects.filter(customer_id=self.request.user)


class AccountList(generics.ListAPIView):
    serializer_class = AccountSerializer
    permissions_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Account.objects.filter(customer_id=self.request.user)
