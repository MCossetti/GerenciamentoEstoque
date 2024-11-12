from django.contrib import admin
from .models import EstoqueEntrada, EstoqueSaida, EstoqueProduto

class EstoqueProdutoInLine(admin.TabularInline):
    model = EstoqueProduto
    extra = 0

@admin.register(EstoqueEntrada)
class EstoqueEntradaAdmin(admin.ModelAdmin):
    inlines = (EstoqueProdutoInLine,)
    list_display=('__str__', 'usuario', 'movimento')
    search_fields=('id',)
    list_filter=('usuario',)
    date_hierarchy='created'

@admin.register(EstoqueSaida)
class EstoqueSaidaAdmin(admin.ModelAdmin):
    inlines = (EstoqueProdutoInLine,)
    list_display=('__str__', 'usuario', 'movimento')
    search_fields=('id',)
    list_filter=('usuario',)
    date_hierarchy='created'
