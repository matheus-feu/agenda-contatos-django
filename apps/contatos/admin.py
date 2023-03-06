from django.contrib import admin

from .models import Contato


# Register your models here.
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria', 'publicada')
    list_display_links = ('id','email')
    search_fields = ('nome', 'sobrenome', 'telefone')
    list_editable = ('telefone', 'publicada')
    list_filter = ('nome', 'categoria')
    list_per_page = 10



admin.site.register(Contato, ContatoAdmin)


