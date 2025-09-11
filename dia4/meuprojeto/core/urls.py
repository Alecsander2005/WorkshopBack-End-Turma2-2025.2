from django.urls import path
from .views import ListarEnderecosView, ViaCepAPIView, CriarEnderecoView, ExcluirEnderecoView

urlpatterns = [
    path('', ListarEnderecosView.as_view(), name='listar_enderecos'),  # Página inicial
    path('api/viacep/', ViaCepAPIView.as_view(), name='viacep_api'),  # API pública ViaCEP
    path('adicionar/', CriarEnderecoView.as_view(), name='adicionar_endereco'),  # Adicionar CEP
    path('deletar/<int:pk>/', ExcluirEnderecoView.as_view(), name='deletar_endereco'),  # Deletar CEP
]