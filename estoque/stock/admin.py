from django.contrib import admin
from .models import Estoque, EstoqueProduto

@admin.register(Estoque)
class ProdutoAdmin(admin.ModelAdmin):
    list_display=('__str__', 'usuario', 'movimento')
    search_fields=('id',)
    list_filter=('usuario',)
    date_hierarchy='created'
