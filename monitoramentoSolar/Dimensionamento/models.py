from django.db import models
from clientes.models import Cliente
from local.models import Local
from modulo.models import Modulo
from inversor.models import Inversor
from geracaoMensal.models import GeracaoMensal

class Dimensionamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='dimensionamentos')
    local = models.ForeignKey(Local, on_delete=models.SET_NULL, null=True, blank=True)
    consumo = models.FloatField()  
    pot_sistema = models.FloatField()  
    geracao_mensal = models.ForeignKey(GeracaoMensal, on_delete=models.SET_NULL, null=True, blank=True)
    modulo = models.ForeignKey(Modulo, on_delete=models.SET_NULL, null=True, blank=True)
    quantidade = models.IntegerField()  
    inversores = models.ManyToManyField(Inversor)
    energia_estimada = models.JSONField(null=True, blank=True) 

    def __str__(self):
        return f"Dimensionamento de {self.cliente.nome} - {self.pot_sistema} kWp"

    def realizar_dimensionamento(self):
        """
        Método para calcular o dimensionamento do sistema fotovoltaico.
        Baseado no consumo mensal e nas características do local e módulos.
        """
       
        if self.modulo and self.pot_sistema:
            potencia_modulo = self.modulo.potencia  
            quantidade_modulos = self.pot_sistema / potencia_modulo
            self.quantidade = round(quantidade_modulos)

            
            if self.local:
                irradiancia_mensal = [
                    self.local.irra_jan, self.local.irra_fev, self.local.irra_mar, self.local.irra_abr,
                    self.local.irra_mai, self.local.irra_jun, self.local.irra_jul, self.local.irra_ago,
                    self.local.irra_set, self.local.irra_out, self.local.irra_nov, self.local.irra_dez
                ]
                # Calculando a geração mensal estimada com base na irradiância do local
                energia_estimativa = []
                for i, irra in enumerate(irradiancia_mensal):
                    energia_estimativa.append(round(irra * self.quantidade * potencia_modulo, 2))

                self.energia_estimada = energia_estimativa

            self.save()  
            return self.energia_estimada

        return None
