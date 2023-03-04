from django.urls import path

from . import views

app_name = 'contatos'

urlpatterns = [
    # GET /
    path('', views.TelaInicialView.as_view(), name='tela_inicial'),

    # GET index
    path('dashboard/', views.HomeView.as_view(), name='dashboard'),

    # GET /contatos
    path('contatos/', views.ContatoListView.as_view(), name='lista_contatos'),

    # GET /contatos/cadastrar
    path('contatos/cadastrar/', views.ContatoCreateView.as_view(), name='cadastrar_contato'),

    # GET /contatos/atualizar/<id>
    path('contatos/atualizar/<pk>', views.ContatoUpdateView.as_view(), name='atualizar_contato'),

    # GET /contatos/excluir/<id>
    path('contatos/excluir/<pk>', views.ContatoDeleteView.as_view(), name='excluir_contato'),

    # GET /contatos/detalhes/<id>
    path('contatos/detalhes/<pk>', views.ContatoDetailView.as_view(), name='detalhes_contato'),

]
