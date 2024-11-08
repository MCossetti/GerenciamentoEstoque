from django.contrib.auth.models import User
from django.db import models
from estoque.core.models import TimeStampedModel
from estoque.produto.models import Produto

MOVIMENTO = (
    ('e', 'entrada'),
    ('s', 'saida'),
)

class Estoque(TimeStampedModel):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    movimento = models.CharField(max_length=1, choices=MOVIMENTO)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f"Estoque #{self.id}"

class EstoqueProduto(models.Model):
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    class Meta:
        unique_together = ('estoque', 'produto')

    def __str__(self):
        return f"{self.produto.nome} - Quantidade: {self.quantidade}"

class HistoricoEstoque(TimeStampedModel):
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    estado = models.CharField(max_length=10)
    observacao = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Histórico {self.id} - Estoque {self.estoque.id}"
    