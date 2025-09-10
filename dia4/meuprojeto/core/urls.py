from django.urls import path
from .views import CriarEnderecoView, ListarEnderecosView, DetalharEnderecoView, ExcluirEnderecoView

urlpatterns = [
    path('', ListarEnderecosView.as_view(), name='listar_enderecos'),  # Lista de endereços
    path('criar/', CriarEnderecoView.as_view(), name='criar_endereco'),  # Criar novo endereço
    path('detalhar/<int:pk>/', DetalharEnderecoView.as_view(), name='detalhar_endereco'),  # Detalhar endereço
    path('excluir/<int:pk>/', ExcluirEnderecoView.as_view(), name='excluir_endereco'),  # Excluir endereço
]