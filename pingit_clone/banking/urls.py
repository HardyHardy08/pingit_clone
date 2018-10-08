from django.urls import path
from . import views

urlpatterns = [
    path('account/', views.AccountListView.as_view(), name='account-list'),
    path('account/create/', views.AccountCreateView.as_view(), name='account-create'),
    path(
        'account/details/<account_number>',
        views.AccountDetailView.as_view(),
        name='account-detail'),
]