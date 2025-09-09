from django.forms import forms
from ...meuprojeto.app2.models import endereco    

class Enderecoform(forms.ModelForm):
    class Meta:
        model = endereco
        fields = ['cep']
        labels = {'cep': 'CEP'}
        widgets = {'cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o CEP'})}  