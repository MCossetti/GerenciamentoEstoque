from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy
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
        return '{} - {}'.format(self.pk, self.created.strftime('%d-%m-%Y'))

    def get_absolute_url(self):
        return reverse_lazy('estoque:estoque_entrada_detail', kwargs={'pk':self.pk})

class EstoqueProduto(models.Model):
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE, related_name='estoques')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField(blank=True, default=0)

    class Meta:
        unique_together = ('estoque', 'produto')

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.estoque.pk, self.produto)

class HistoricoEstoque(TimeStampedModel):
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    estado = models.CharField(max_length=10)
    observacao = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Histórico {self.id} - Estoque {self.estoque.id}"
    