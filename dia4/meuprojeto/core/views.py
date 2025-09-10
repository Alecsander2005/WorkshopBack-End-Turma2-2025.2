import requests
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, DeleteView, DetailView
from .models import endereco
from .forms import enderecoform

class CriarEnderecoView(FormView):
    template_name = 'form_endereco.html'
    form_class = enderecoform
    success_url = reverse_lazy('listar_enderecos')

    def form_valid(self, form):
        cep = form.cleaned_data['cep']
        # Faz a requisição para a API ViaCEP
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if response.status_code == 200:
            dados = response.json()
            if 'erro' not in dados:
                # Cria o objeto endereco com os dados retornados pela API
                endereco.objects.create(
                    cep=cep,
                    rua=dados.get('logradouro', ''),
                    bairro=dados.get('bairro', ''),
                    cidade=dados.get('localidade', ''),
                    estado=dados.get('uf', '')
                )
                return super().form_valid(form)
            else:
                form.add_error('cep', 'CEP inválido.')
        else:
            form.add_error('cep', 'Erro ao buscar o CEP. Tente novamente.')
        return super().form_invalid(form)

class ListarEnderecosView(ListView):
    model = endereco
    template_name = 'listar_enderecos.html'
    context_object_name = 'enderecos'

class DetalharEnderecoView(DetailView):
    model = endereco
    template_name = 'detalhar_endereco.html'
    context_object_name = 'endereco'

class ExcluirEnderecoView(DeleteView):
    model = endereco
    template_name = 'confirmar_exclusao.html'
    success_url = reverse_lazy('listar_enderecos')