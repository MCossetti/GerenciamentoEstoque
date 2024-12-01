from django.contrib.auth.models import User
from django.db import models
from estoque.core.models import TimeStampedModel
from estoque.produto.models import Produto
from .managers import EstoqueEntradaManager, EstoqueSaidaManager

MOVIMENTO = (
    ('e', 'entrada'),
    ('s', 'saida'),
)

class Estoque(TimeStampedModel):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    movimento = models.CharField(max_length=1, choices=MOVIMENTO, blank=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return '{}'.format(self.pk)
   
class EstoqueEntrada(Estoque):
    objects = EstoqueEntradaManager()

    class Meta:
        proxy=True
        verbose_name = 'Estoque entrada'
        verbose_name_plural = 'Estoque entrada'  
 
class EstoqueSaida(Estoque):
    objects = EstoqueSaidaManager()

    class Meta:
        proxy=True
        verbose_name = 'Estoque saida'
        verbose_name_plural = 'Estoque saida'

class EstoqueProduto(models.Model):
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE, related_name='estoques')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField(blank=True, default=0)

    class Meta:
        unique_together = ('estoque', 'produto')

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.estoque.pk, self.produto)