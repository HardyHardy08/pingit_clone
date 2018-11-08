from rest_framework import permissions, viewsets
from banking.serializers import AccountSerializer
from banking.models import Account
from .permissions import IsOwner


class AccountViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AccountSerializer
    lookup_field = 'account_number'
    permission_classes = (permissions.IsAuthenticated, IsOwner,)

    def get_queryset(self):
        return Account.objects.filter(customer_id=self.request.user)
