import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import AccountCreationForm, TransactionCreationForm

from .models import Account, Transaction


class AccountCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'account/create.html'
    form_class = AccountCreationForm

    def form_valid(self, form):
        self.object = Account.objects.create_account(
            account_type_code=form.cleaned_data['account_type_code'],
            customer=self.request.user,
            starting_balance=100
        )
        return HttpResponseRedirect(reverse_lazy(
            'banking:account-detail',
            kwargs={'account_number': self.object.account_number}))


class AccountListView(LoginRequiredMixin, generic.ListView):
    model = Account
    template_name = 'account/index.html'
    context_object_name = 'account_list'

    def get_queryset(self):
        queryset = Account.objects.filter(customer_id=self.request.user)
        return queryset


class AccountDetailView(LoginRequiredMixin, generic.DetailView):
    model = Account
    template_name = 'account/detail.html'
    context_object_name = 'account'
    slug_field = 'account_number'
    slug_url_kwarg = 'account_number'

    def get_queryset(self):
        queryset = Account.objects.filter(customer_id=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        transaction_list = self.object.transaction_set.all()
        for transaction in transaction_list:
            transaction.other_details = json.loads(transaction.other_details)
        context['transaction_list'] = transaction_list
        return context


class TransactionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Transaction
    template_name = 'transaction/create.html'
    form_class = TransactionCreationForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(user=self.request.user, **self.get_form_kwargs())

    def form_valid(self, form):
        self.object = Transaction.objects.create_transfer_transaction(**form.cleaned_data)
        return HttpResponseRedirect(reverse_lazy(
            'banking:account-detail',
            kwargs={'account_number': self.object.source.account_number}))
