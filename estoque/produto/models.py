from django.db import models

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
