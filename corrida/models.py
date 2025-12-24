from django.db import models
from usuarios.models import Cliente, Mototaxista
from core.models import BaseModel, StatusCorrida



class Corrida(BaseModel):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    mototaxista = models.ForeignKey(Mototaxista, on_delete=models.SET_NULL, null=True, blank=True)
    origem = models.CharField(max_length=255)
    destino = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=StatusCorrida.choices, default=StatusCorrida.SOLICITADA)


    def __str__(self):
        return f"Corrida {self.id} - {self.status}"