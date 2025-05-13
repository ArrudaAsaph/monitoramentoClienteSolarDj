from django.db import models
from clientes.models import Cliente

class GeracaoMensal(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    ano = models.IntegerField()
    janeiro = models.FloatField(default=0)
    fevereiro = models.FloatField(default=0)
    marco = models.FloatField(default=0)
    abril = models.FloatField(default=0)
    maio = models.FloatField(default=0)
    junho = models.FloatField(default=0)
    julho = models.FloatField(default=0)
    agosto = models.FloatField(default=0)
    setembro = models.FloatField(default=0)
    outubro = models.FloatField(default=0)
    novembro = models.FloatField(default=0)
    dezembro = models.FloatField(default=0)

    def __str__(self):
        return f"Geração de {self.cliente.nome} - {self.ano}"
