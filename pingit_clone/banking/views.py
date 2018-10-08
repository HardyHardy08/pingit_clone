"""
TODO:
    - APIfy the models
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import AccountCreationForm

from .models import Account


class AccountCreateView(generic.View):
    success_url = reverse_lazy('account-detail')
    template_name = 'account/create.html'
    form_class = AccountCreationForm

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_account = Account.objects.create_account(
                account_type_code=form.cleaned_data['account_type_code'],
                customer=request.user,
                starting_balance=100
            )
            return HttpResponseRedirect(reverse_lazy(
                'banking:account-detail',
                kwargs={'account_number': new_account.account_number}))
        return HttpResponseRedirect(reverse_lazy('account-create'))


class AccountListView(LoginRequiredMixin, generic.ListView):
    model = Account
    template_name = 'account/index.html'

    def get_queryset(self):
        queryset = Account.objects.filter(customer_id=self.request.user)
        return queryset


class AccountDetailView(LoginRequiredMixin, generic.DetailView):
    model = Account
    template_name = 'account/detail.html'
    slug_field = 'account_number'
    slug_url_kwarg = 'account_number'
