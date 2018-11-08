import json
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from banking.serializers import AccountSerializer, TransactionSerializer
from banking.models import Account
from .permissions import IsOwner


class AccountViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AccountSerializer
    lookup_field = 'account_number'
    permission_classes = (permissions.IsAuthenticated, IsOwner,)

    def get_queryset(self):
        return Account.objects.filter(customer_id=self.request.user)


class TransactionCreate(viewsets.ViewSet):
    permissions_classes = (permissions.IsAuthenticated,)

    def _create_error_message(self, serializer):
        message = {"error_message": "Invalid fields."}
        message['errors'] = {}
        for field, error in serializer.errors.items():
            message['errors'][field] = error.pop().code
        return json.dumps(message)

    def create(self, request, format=None):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(self._create_error_message(serializer),
                            status=status.HTTP_400_BAD_REQUEST)
