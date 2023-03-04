from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render
from django.db.models import Q

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, DetailView

from .models import Contato
from .forms import InsereContatoForm, AtualizaContatoForm

from django.contrib.auth.mixins import LoginRequiredMixin


class TelaInicialView(TemplateView):
    """Inicia-se na página na pagina inicial do site"""
    template_name = 'telainicial.html'


class HomeView(LoginRequiredMixin, TemplateView):
    """Página inicial do site"""
    template_name = 'dashboard.html'


class ContatoDetailView(LoginRequiredMixin, DetailView):
    """Página de detalhes de contatos"""
    template_name = 'detalhes.html'
    model = Contato


class ContatoListView(LoginRequiredMixin, ListView):
    """Página de listagem de contatos, permite buscar os contatos da agenda e paginação entre eles
    função get_queryset() é responsável por buscar os contatos por nome, telefone e email,
    Q() é um operador lógico do Django que permite fazer buscas por vários campos ao mesmo tempo"""

    template_name = 'contatos.html'
    model = Contato
    context_object_name = 'contatos'
    paginate_by = 3

    def get_queryset(self):
        """Busca os contatos por nome, telefone e email,
        retornando na lista de contatos"""
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)

        search = self.request.GET.get('search')

        # Busca os contatos por nome, telefone e email
        if search:
            qs = qs.filter(
                Q(nome__icontains=search) | Q(telefone__icontains=search) | Q(email__icontains=search))

        return qs


class ContatoUpdateView(LoginRequiredMixin, UpdateView):
    """Página de atualização de contatos, valida se o formulário é
    válido e envia uma mensagem de sucesso na página da lista de contatos"""

    template_name = 'atualiza.html'
    model = Contato
    form_class = AtualizaContatoForm
    success_url = reverse_lazy('contatos:lista_contatos')

    def form_valid(self, form):
        messages.warning(self.request, 'Contato atualizado com sucesso!')
        return super().form_valid(form)


class ContatoCreateView(LoginRequiredMixin, CreateView):
    """Página de cadastro de contatos, se o formulário for válido,
    retorna uma mensagem de sucesso"""

    template_name = 'cria.html'
    model = Contato
    form_class = InsereContatoForm
    success_url = reverse_lazy('contatos:lista_contatos')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.info(self.request, 'Contato cadastrado com sucesso!')
        return super().form_valid(form)


class ContatoDeleteView(LoginRequiredMixin, DeleteView):
    """Página de exclusão de contatos, se o formulário for válido,
    retorna uma mensagem de sucesso que o contato foi excluído"""

    template_name = 'exclui.html'
    model = Contato
    context_object_name = 'contato'
    success_url = reverse_lazy('contatos:lista_contatos')

    def form_valid(self, form):
        messages.error(self.request, 'Contato excluído com sucesso!')
        return super().form_valid(form)


def handler404(request, exception):
    """Página de erro 404 caso o usuário tente acessar uma página que não existe"""
    return render(request, 'errors/404.html', status=404)
