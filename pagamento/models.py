from django.db import models
from corrida.models import Corrida
from core.models import BaseModel, StatusPagamento



class Pagamento(BaseModel):
    corrida = models.OneToOneField(Corrida, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=StatusPagamento.choices, default=StatusPagamento.PENDENTE)
    referencia = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return f"Pagamento {self.id} - {self.status}"