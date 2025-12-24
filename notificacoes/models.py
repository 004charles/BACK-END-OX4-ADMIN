from django.db import models
from usuarios.models import Usuario
from core.models import BaseModel



class Notificacao(BaseModel):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    mensagem = models.TextField()
    lida = models.BooleanField(default=False)


    def __str__(self):
        return self.titulo