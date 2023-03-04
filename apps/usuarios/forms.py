from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    """Formulário de cadastro de usuários, classe responsável de criar os campos do formulário e validar os dados"""
    first_name = forms.CharField(label="Nome de cadastro", required=True, max_length=30, widget=forms.TextInput)
    last_name = forms.CharField(label="Sobrenome", required=True, max_length=30, widget=forms.TextInput)
    username = forms.CharField(label="Usuário", required=True, max_length=30, widget=forms.TextInput)
    email = forms.EmailField(label="E-mail", required=True, max_length=30, widget=forms.TextInput)
    password1 = forms.CharField(label="Senha", required=True, max_length=30, widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme a senha", required=True, max_length=30, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if ' ' in first_name:
            raise forms.ValidationError('Usuário não pode conter espaços em branco')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if ' ' in last_name:
            raise forms.ValidationError('Sobrenome não pode conter espaços em branco')
        return last_name

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Usuário já existe')
        elif ' ' in username:
            raise forms.ValidationError('Usuário não pode conter espaços em branco')
        return username


