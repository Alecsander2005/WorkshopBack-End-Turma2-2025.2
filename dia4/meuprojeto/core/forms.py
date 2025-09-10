from django import forms
from .models import endereco

class enderecoform(forms.ModelForm):  # Nome do formulário com "e" minúsculo
    class Meta:
        model = endereco
        fields = ['cep']  # Apenas o campo CEP será exibido no formulário
        labels = {'cep': 'CEP'}
        widgets = {
            'cep': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o CEP'
            })
        }