from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Usuario, Moto
from .serializers import (
    UsuarioSerializer,
    RegistroClienteSerializer,
    RegistroMototaxistaSerializer,
    MotoSerializer
)


class PerfilUsuarioView(generics.RetrieveAPIView):
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class RegistroClienteView(generics.CreateAPIView):
    serializer_class = RegistroClienteSerializer
    permission_classes = [permissions.AllowAny]


class RegistroMototaxistaView(generics.CreateAPIView):
    serializer_class = RegistroMototaxistaSerializer
    permission_classes = [permissions.AllowAny]


class MotoCreateListView(generics.ListCreateAPIView):
    serializer_class = MotoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Moto.objects.filter(mototaxista__usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(
            mototaxista=self.request.user.mototaxista
        )
