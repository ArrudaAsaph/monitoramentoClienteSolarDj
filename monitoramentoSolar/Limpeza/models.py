from http import client
from django.db import models
from datetime import time
from clientes.models import Cliente
# Create your models here.

class Limpeza(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="limpezas")
    data_limpeza = models.DateTimeField()
    valor = models.FloatField()
    tempo = models.TimeField()
    dificuldade = models.IntegerField()

    def __str__(self):
        return f"Limpeza de {self.cliente.nome} em {self.data_limpeza.date()}"