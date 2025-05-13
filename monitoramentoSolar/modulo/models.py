from django.db import models

# Create your models here.
class Modulo(models.Model):
    potencia = models.IntegerField()
    marca = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.marca} - {self.potencia}W"