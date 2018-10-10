from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import AccountCreationForm

from .models import Account


class AccountCreateView(generic.CreateView):
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
