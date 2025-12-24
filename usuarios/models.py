from django.contrib.auth.models import AbstractUser
from django.db import models
from core.models import BaseModel


class Usuario(AbstractUser):
    e_cliente = models.BooleanField(default=False)
    e_mototaxista = models.BooleanField(default=False)




class Cliente(BaseModel):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.usuario.username




class Mototaxista(BaseModel):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20)
    verificado = models.BooleanField(default=False)


    def __str__(self):
        return self.usuario.username




class Moto(BaseModel):
    mototaxista = models.ForeignKey(Mototaxista, on_delete=models.CASCADE)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    matricula = models.CharField(max_length=20)


    def __str__(self):
        return f"{self.marca} {self.modelo}"