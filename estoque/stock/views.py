from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, View
from estoque.produto.models import Produto
from .forms import EstoqueForm, EstoqueProdutoForm
from .models import Estoque, EstoqueEntrada, EstoqueSaida, EstoqueProduto

@method_decorator(login_required, name='dispatch')
class EstoqueEntradaList(ListView):
    model = EstoqueEntrada
    template_name = 'estoque_list.html'
    def get_context_data(self, **kwargs):
        context = super(EstoqueEntradaList, self).get_context_data(**kwargs)
        context['titulo'] = 'Entrada'
        context['url_add'] = 'estoque:estoque_entrada_add'
        return context

class EstoqueDetail(DetailView):
    model = Estoque
    template_name = 'estoque_detail.html'

class DarBaixaEstoque(View):
    @staticmethod
    def dar_baixa_estoque(form):
        produtos = form.estoques.all()
        for item in produtos:
            produto = Produto.objects.get(pk=item.produto.pk)
            produto.estoque = item.saldo
            produto.save()
        print('Estoque atualizado com sucesso.')

@method_decorator(login_required, name='dispatch')
class EstoqueAddView(View):
    template_name = None
    movimento = None
    url_redirect = None

    def get_context_data(self, form, formset):
        return {'form': form, 'formset': formset}

    def get(self, request):
        estoque_form = Estoque()
        item_estoque_formset = inlineformset_factory(
            Estoque,
            EstoqueProduto,
            form=EstoqueProdutoForm,
            extra=0,
            can_delete=False,
            min_num=1,
            validate_min=True,
        )
        form = EstoqueForm(instance=estoque_form, prefix='main')
        formset = item_estoque_formset(instance=estoque_form, prefix='estoque')
        context = self.get_context_data(form, formset)
        return render(request, self.template_name, context)

    def post(self, request):
        estoque_form = Estoque()
        item_estoque_formset = inlineformset_factory(
            Estoque,
            EstoqueProduto,
            form=EstoqueProdutoForm,
            extra=0,
            can_delete=False,
            min_num=1,
            validate_min=True,
        )
        form = EstoqueForm(request.POST, instance=estoque_form, prefix='main')
        formset = item_estoque_formset(request.POST, instance=estoque_form, prefix='estoque')
        
        if form.is_valid() and formset.is_valid():
            form = form.save(commit=False)
            form.usuario = request.user
            form.movimento = self.movimento
            form.save()
            formset.save()
            DarBaixaEstoque.dar_baixa_estoque(form)
            return HttpResponseRedirect(resolve_url(self.url_redirect, form.pk))
        
        context = self.get_context_data(form, formset)
        return render(request, self.template_name, context)


@method_decorator(login_required, name='dispatch')
class EstoqueEntradaAdd(EstoqueAddView):
    template_name = 'estoque_entrada_form.html'
    movimento = 'e'
    url_redirect = 'estoque:estoque_detail'

@method_decorator(login_required, name='dispatch')
class EstoqueSaidaList(ListView):
    model = EstoqueSaida
    template_name = 'estoque_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Saída'
        context['url_add'] = 'estoque:estoque_saida_add'
        return context

@method_decorator(login_required, name='dispatch')
class EstoqueSaidaAdd(EstoqueAddView):
    template_name = 'estoque_saida_form.html'
    movimento = 's'
    url_redirect = 'estoque:estoque_detail'