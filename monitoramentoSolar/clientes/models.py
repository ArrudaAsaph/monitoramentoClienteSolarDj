from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=250)
    data_instalacao = models.DateField()

    email = models.EmailField(blank=True, null=True)
    senha = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.nome