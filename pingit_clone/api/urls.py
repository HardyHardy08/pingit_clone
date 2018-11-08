from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('account/<str:account_number>', views.AccountDetail.as_view(), name="account-detail"),
    path('account/', views.AccountList.as_view(), name="account-list"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
