from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('endereco/', views.endereco, name='endereco'),  # Página de endereço
]