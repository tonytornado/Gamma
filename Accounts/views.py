from django.contrib.auth import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import login, logout
from django.urls import reverse_lazy
from django.views import generic

import Accounts
from Accounts.models import User


class LoginView(generic.FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')
    template_name = 'form.html'

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request, **self.get_form_kwargs())

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


class LogoutView(generic.RedirectView):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class Register(generic.CreateView):
    form_class = forms.UserCreationForm
    success_url = reverse_lazy('login')


class AccountView(generic.DetailView):
    model = User
    context_object_name = 'users'
    template_name = "user_page.html"


class EditView(generic.UpdateView):
    model = Accounts.models.User
    fields = ['display_name', 'avatar', 'bio']
    template_name = 'form.html'
    success_url = reverse_lazy('user_profile', {'pk': User.pk})
