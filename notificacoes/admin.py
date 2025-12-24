from django.contrib import admin
from .models import Notificacao


@admin.register(Notificacao)
class NotificacaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'usuario', 'lida', 'criado_em')
    list_filter = ('lida',)
    search_fields = ('titulo', 'usuario__username')
