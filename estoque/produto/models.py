from django.db import models
from django.urls import reverse_lazy

class Produto(models.Model): 
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200, blank=True, null=True)
    preco = models.DecimalField('preço', max_digits=10, decimal_places=2)
    estoque = models.IntegerField('estoque atual')
    estoque_minimo = models.PositiveIntegerField('estoque mínimo', default=0)

    class Meta:
        ordering = ('nome',)
    
    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse_lazy('produto:produto_detail', kwargs={'pk':self.pk})
