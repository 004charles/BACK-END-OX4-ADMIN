from django.contrib import admin
from .models import Usuario, Cliente, Mototaxista, Moto


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'e_cliente', 'e_mototaxista', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('e_cliente', 'e_mototaxista', 'is_staff')


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'telefone', 'criado_em')
    search_fields = ('usuario__username', 'telefone')


@admin.register(Mototaxista)
class MototaxistaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'telefone', 'verificado', 'criado_em')
    list_filter = ('verificado',)
    search_fields = ('usuario__username', 'telefone')


@admin.register(Moto)
class MotoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'matricula', 'mototaxista')
    search_fields = ('marca', 'modelo', 'matricula')
