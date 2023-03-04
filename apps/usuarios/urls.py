from django.urls import path
from . import views


app_name = 'usuarios'

urlpatterns = [
    path('register/', views.SignUpView.as_view(), name='cadastrar_usuario'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
]
