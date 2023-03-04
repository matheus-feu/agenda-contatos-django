from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib.auth.views import LogoutView as DjangoLogoutView

from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm


# Create your views here.
class SignUpView(generic.CreateView):
    """Template de cadastro de usuários"""
    form_class = SignUpForm
    success_url = reverse_lazy('usuarios:login')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        messages.success(self.request, 'Usuário cadastrado com sucesso!')
        return super().form_valid(form)


class LoginView(DjangoLoginView):
    """Template de login de usuários"""
    template_name = 'registration/login.html'
    success_url = reverse_lazy('contatos:dashboard')

    def get_success_url(self):
        """Retorna a página de lista de contatos após o usuário fazer o login"""
        return self.success_url or super().get_success_url()


class LogoutView(DjangoLogoutView):
    """Retorna a pagina de login após o usuário fazer o logout"""
    next_page = reverse_lazy('usuarios:login')
