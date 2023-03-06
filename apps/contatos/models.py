from django.db import models
from stdimage import StdImageField

from django.contrib.auth import get_user_model
from .choices import *


# Create your models here.
class Contato(models.Model):
    """Classe que representa os dados do contato no banco de dados"""
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE) # Relacionamento com o usuário, para que cada usuário tenha seus contatos
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=150, blank=True)
    telefone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=150, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField(blank=True)
    categoria = models.CharField(choices=CATEGORIA_CHOICES, max_length=150)
    publicada = models.BooleanField(default=False)
    avatar = StdImageField('Avatar', blank=True, null=True, delete_orphans=True, upload_to='avatars/%Y/%m/%d/')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        ordering = ['nome']
