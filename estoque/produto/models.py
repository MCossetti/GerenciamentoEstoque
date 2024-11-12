from django.db import models
from django.urls import reverse_lazy

class Produto(models.Model): 
    nome = models.CharField('Nome:', max_length=100)
    descricao = models.CharField('Descrição:', max_length=200, blank=True, null=True)
    preco = models.DecimalField('Preço:', max_digits=10, decimal_places=2)
    estoque = models.IntegerField('Estoque Atual:')
    estoque_minimo = models.PositiveIntegerField('Estoque Mínimo:', default=0)

    class Meta:
        ordering = ('nome',)
    
    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse_lazy('produto:produto_detail', kwargs={'pk':self.pk})

    def to_dict_json(self):
        return {
            'pk': self.pk,
            'produto': self.nome,
            'estoque':self.estoque,
        }
