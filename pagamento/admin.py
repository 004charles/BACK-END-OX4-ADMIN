from django.contrib import admin
from .models import Pagamento


@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'corrida', 'valor', 'status', 'metodo', 'criado_em')
    list_filter = ('status', 'metodo')
