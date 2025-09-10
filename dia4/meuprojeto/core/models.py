from django.db import models

class endereco(models.Model):  # Nome do modelo com "e" minúsculo
    cep = models.CharField(max_length=8)  # Exemplo: "01001000"
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)  # Exemplo: "SP"

    def __str__(self):
        return f"{self.rua}, {self.bairro}, {self.cidade} - {self.estado}, CEP: {self.cep}"