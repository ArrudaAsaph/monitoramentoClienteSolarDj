from django.db import models

# Create your models here.
class Inversor(models.Model):
    modelo = models.CharField(max_length=100)
    potencia_maxima = models.FloatField()  # em kW
    fases = models.IntegerField(choices=[(1, 'Monofásico'), (2, 'Bifásico'), (3, 'Trifásico')])

    def __str__(self):
        return f"{self.modelo} - {self.potencia_maxima}kW - {self.fases} fases"