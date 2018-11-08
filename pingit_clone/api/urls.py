from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

account_list = views.AccountViewSet.as_view({
    'get': 'list',
})
account_detail = views.AccountViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    path('account/<str:account_number>', account_detail, name="account-detail"),
    path('account/', account_list, name="account-list"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
