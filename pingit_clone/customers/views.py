from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomerCreationForm


class SignUp(generic.CreateView):
    form_class = CustomerCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'

    def form_valid(self, form):
        """If the form is valid, save the model, login user, and redirect to success URL."""
        self.object = form.save()
        login(self.request, self.object)
        return HttpResponseRedirect(self.get_success_url())
