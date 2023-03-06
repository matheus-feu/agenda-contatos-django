from django import forms
# from django.utils import timezone
from django.forms import Textarea
from stdimage import StdImageField

from .choices import *
from .models import Contato


class InsereContatoForm(forms.ModelForm):
    """Esta classe é responsável por criar o formulário de inserção de contatos."""
    nome = forms.CharField(label='Nome', max_length=150,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}))
    sobrenome = forms.CharField(label='Sobrenome', max_length=150, required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sobrenome'}))
    telefone = forms.CharField(label='Telefone', max_length=15,
                               widget=forms.TextInput(attrs={'placeholder': '(11) 99999-9999'}))
    email = forms.EmailField(label='E-mail', max_length=150, required=False)
    descricao = forms.CharField(label='Descrição', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    categoria = forms.ChoiceField(label='Categoria', choices=CATEGORIA_CHOICES)
    publicada = forms.BooleanField(label='Publicada', required=False, initial=False, widget=forms.CheckboxInput())
    avatar = StdImageField('Avatar', upload_to='Avatars/%Y/%m/%d/')

    class Meta:
        model = Contato
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'descricao': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

    def __init__(self, *args, **kwargs):
        """Esta função acrescente a opção 'Selecione uma categoria' no campo categoria do formulário de inserção de contatos.
        Sendo obrigada a escolher uma categoria para o contato ser inserido no banco de dados."""
        super().__init__(*args, **kwargs)
        self.fields['categoria'].choices = [('', 'Selecione uma categoria')] + CATEGORIA_CHOICES

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('O nome não pode conter espaços.')
            elif any(char.isdigit() for char in nome):
                raise forms.ValidationError('O nome não pode conter números.')
            else:
                return nome

    def clean_sobrenome(self):
        sobrenome = self.cleaned_data.get('sobrenome')

        if sobrenome:
            sobrenome = sobrenome.strip()
            if ' ' in sobrenome:
                raise forms.ValidationError('O sobrenome não pode conter espaços')
            elif any(char.isdigit() for char in sobrenome):
                raise forms.ValidationError('O sobrenome não pode conter números')
            else:
                return sobrenome


class AtualizaContatoForm(forms.ModelForm):
    """Esta classe é responsável por criar o formulário de atualização de contatos."""
    nome = forms.CharField(label='Nome', max_length=150,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}))
    sobrenome = forms.CharField(label='Sobrenome', max_length=150, required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sobrenome'}))
    telefone = forms.CharField(label='Telefone', max_length=15,
                               widget=forms.TextInput(attrs={'placeholder': '(11) 99999-9999'}))
    email = forms.EmailField(label='E-mail', max_length=150, required=False)
    # data_criacao = forms.DateTimeField(label='Data de criação',widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'readonly':True}, format='%Y-%m-%dT%H:%M'), initial=timezone.now)
    descricao = forms.CharField(label='Descrição', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    categoria = forms.ChoiceField(label='Categoria', choices=CATEGORIA_CHOICES)
    publicada = forms.BooleanField(label='Publicada', required=False, initial=True,
                                   widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    avatar = StdImageField('Avatar', upload_to='Avatars/%Y/%m/%d/')

    class Meta:
        model = Contato
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'descricao': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

    def __init__(self, *args, **kwargs):
        """Esta função acrescente a opção 'Selecione uma categoria' no campo categoria do formulário de inserção de contatos.
        Sendo obrigada a escolher uma categoria para o contato ser inserido no banco de dados."""
        super().__init__(*args, **kwargs)
        self.fields['categoria'].choices = [('', 'Selecione uma categoria')] + CATEGORIA_CHOICES

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('O nome não pode conter espaços')
            elif any(char.isdigit() for char in nome):
                raise forms.ValidationError('O nome não pode conter números')
            else:
                return nome
