import requests
from django.shortcuts import render

def home(request):
    # Renderiza o template home.html
    return render(request, 'home.html')

def endereco(request):
    # Obtém o CEP enviado pelo formulário
    cep = request.GET.get('cep')
    endereco = None

    if cep:
        # Faz uma requisição à API ViaCEP para buscar o endereço
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if response.status_code == 200:
            endereco = response.json()
            # Verifica se o CEP é válido
            if 'erro' in endereco:
                endereco = None

    # Renderiza o template endereco.html com os dados do endereço
    return render(request, 'endereco.html', {'endereco': endereco})