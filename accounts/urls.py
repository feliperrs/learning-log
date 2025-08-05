"""Define padroes de URL para contas"""

from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    # Inclui URLs de autenticacao default
    path('', include('django.contrib.auth.urls')),
    # Pagina de cadastro
    path('register/', views.register, name='register')
]