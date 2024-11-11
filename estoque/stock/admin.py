from django.contrib import admin
from .models import Estoque, EstoqueProduto


class EstoqueProdutoInLine(admin.TabularInline):
    model = EstoqueProduto
    extra = 0

@admin.register(Estoque)
class ProdutoAdmin(admin.ModelAdmin):
    inlines = (EstoqueProdutoInLine,)
    list_display=('__str__', 'usuario', 'movimento')
    search_fields=('id',)
    list_filter=('usuario',)
    date_hierarchy='created'
