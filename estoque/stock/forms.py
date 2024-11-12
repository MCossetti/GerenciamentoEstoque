from django import forms
from .models import Estoque, EstoqueProduto

class EstoqueForm(forms.ModelForm):

    class Meta:
        model = Estoque
        fields = '__all__'

class EstoqueProdutoForm(forms.ModelForm):

    class Meta:
        model = EstoqueProduto
        fields = '__all__'

