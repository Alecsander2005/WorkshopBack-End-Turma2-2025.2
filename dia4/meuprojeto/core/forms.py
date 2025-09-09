from django.forms import forms
from ...meuprojeto.core.models import endereco    

class Enderecoform(forms.ModelForm):
    class Meta:
        model = endereco
        fields = ['cep']
        labels = {'cep': 'CEP'}
        widgets = {'cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o CEP'})}  