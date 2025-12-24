from django.contrib import admin
from .models import Corrida


@admin.register(Corrida)
class CorridaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'cliente',
        'mototaxista',
        'status',
        'preco',
        'criado_em'
    )
    list_filter = ('status',)
    search_fields = ('cliente__usuario__username', 'mototaxista__usuario__username')
