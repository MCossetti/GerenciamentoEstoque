from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = '__all__'

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if Produto.objects.filter(nome=nome).exists():
            raise forms.ValidationError("Já existe um produto com este nome.")
        return nome