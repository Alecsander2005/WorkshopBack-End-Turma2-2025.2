from rest_framework import serializers
from .models import endereco

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = endereco
        fields = ['id', 'cep', 'rua', 'bairro', 'cidade', 'estado']