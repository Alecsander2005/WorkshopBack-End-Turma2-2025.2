import requests
from django.views.generic import ListView, CreateView, DeleteView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.urls import reverse_lazy
from .models import endereco
from .forms import enderecoform
from .serializers import EnderecoSerializer

class ListarEnderecosView(ListView):
    
    model = endereco
    template_name = 'listar_enderecos.html'
    context_object_name = 'enderecos'

class CriarEnderecoView(CreateView):
    
    model = endereco
    form_class = enderecoform
    template_name = 'form_endereco.html'
    success_url = reverse_lazy('listar_enderecos')

    def form_valid(self, form):
        cep = form.cleaned_data['cep']
        # Faz a requisição para a API ViaCEP
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if response.status_code == 200:
            dados = response.json()
            if 'erro' not in dados:
                # Preenche os campos do modelo com os dados retornados pela API
                self.object = form.save(commit=False)
                self.object.rua = dados.get('logradouro', '')
                self.object.bairro = dados.get('bairro', '')
                self.object.cidade = dados.get('localidade', '')
                self.object.estado = dados.get('uf', '')
                self.object.save()
                return super().form_valid(form)
            else:
                form.add_error('cep', 'CEP inválido.')
        else:
            form.add_error('cep', 'Erro ao buscar o CEP. Tente novamente.')
        return super().form_invalid(form)

class ExcluirEnderecoView(DeleteView):
    model = endereco
    template_name = 'confirmar_exclusao.html'
    success_url = reverse_lazy('listar_enderecos')

class ViaCepAPIView(APIView):
    
    def get(self, request):
        # Retorna todos os endereços cadastrados no banco de dados
        enderecos = endereco.objects.all()
        serializer = EnderecoSerializer(enderecos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Recebe um CEP e adiciona um novo endereço ao banco de dados
        cep = request.data.get('cep')
        if not cep:
            return Response({'erro': 'O campo CEP é obrigatório.'}, status=status.HTTP_400_BAD_REQUEST)

        # Faz a requisição para a API ViaCEP
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if response.status_code == 200:
            dados = response.json()
            if 'erro' not in dados:
                # Cria um novo registro no banco de dados
                endereco_obj = endereco.objects.create(
                    cep=cep,
                    rua=dados.get('logradouro', ''),
                    bairro=dados.get('bairro', ''),
                    cidade=dados.get('localidade', ''),
                    estado=dados.get('uf', '')
                )
                serializer = EnderecoSerializer(endereco_obj)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'erro': 'CEP inválido.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'erro': 'Erro ao buscar o CEP.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)