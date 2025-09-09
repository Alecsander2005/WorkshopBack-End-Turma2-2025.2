from django.db import models

class endereco(models.Model):
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    cep = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.rua}, {self.bairro}, {self.cidade} - {self.estado}, {self.cep}"
# Create your models here.
