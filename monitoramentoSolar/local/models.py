from django.db import models

# Create your models here.
class Local(models.Model):
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)

    irra_jan = models.FloatField()
    irra_fev = models.FloatField()
    irra_mar = models.FloatField()
    irra_abr = models.FloatField()
    irra_mai = models.FloatField()
    irra_jun = models.FloatField()
    irra_jul = models.FloatField()
    irra_ago = models.FloatField()
    irra_set = models.FloatField()
    irra_out = models.FloatField()
    irra_nov = models.FloatField()
    irra_dez = models.FloatField()


def __str__(self):
        return f"{self.cidade} - {self.estado}"


def media_anual(self):
        valores = [
            self.irra_jan, self.irra_fev, self.irra_mar, self.irra_abr,
            self.irra_mai, self.irra_jun, self.irra_jul, self.irra_ago,
            self.irra_set, self.irra_out, self.irra_nov, self.irra_dez
        ]
        return round(sum(valores) / 12, 2)