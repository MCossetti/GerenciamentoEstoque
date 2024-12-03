from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from django.views import View
from django.views.generic import ListView, DetailView
from estoque.produto.models import Produto
from .forms import EstoqueForm, EstoqueProdutoForm
from .models import Estoque, EstoqueEntrada, EstoqueSaida, EstoqueProduto
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class EstoqueEntradaList(ListView):
    model = EstoqueEntrada
    template_name = 'estoque_list.html'

    def get_queryset(self):
        return EstoqueEntrada.objects.all().order_by('-created')
    
    def get_context_data(self, **kwargs):
        context = super(EstoqueEntradaList, self).get_context_data(**kwargs)
        context['titulo'] = 'Entrada'
        context['url_add'] = 'estoque:estoque_entrada_add'
        return context

class EstoqueDetail(DetailView):
    model = Estoque
    template_name = 'estoque_detail.html'

class EstoqueBaixa(View):
    def __init__(self, form):
        self.form = form

    def atualizar_estoque(self):
        produtos = self.form.estoques.all()
        for item in produtos:
            produto = Produto.objects.get(pk=item.produto.pk)
            produto.estoque = item.saldo
            produto.save()
        print('Estoque atualizado com sucesso.')

class EstoqueAdd(View):
    template_name = None
    movimento = None
    url = "estoque:estoque_detail"

    def get_item_estoque_formset(self):
        return inlineformset_factory(
            Estoque,
            EstoqueProduto,
            form=EstoqueProdutoForm,
            extra=0,
            can_delete=False,
            min_num=1,
            validate_min=True,
        )

    def get_context_data(self, form, formset):
        return {"form": form, "formset": formset}

    def post(self, request, *args, **kwargs):
        estoque_form = Estoque()
        item_estoque_formset = self.get_item_estoque_formset()

        form = EstoqueForm(
            request.POST,
            instance=estoque_form,
            prefix="main",
        )
        formset = item_estoque_formset(
            request.POST,
            instance=estoque_form,
            prefix="estoque",
        )

        if form.is_valid() and formset.is_valid():
            estoque = form.save(commit=False)
            estoque.usuario = request.user
            estoque.movimento = self.movimento
            estoque.save()
            formset.instance = estoque
            formset.save()
            EstoqueBaixa(estoque).atualizar_estoque()
            return HttpResponseRedirect(resolve_url(self.url, estoque.pk))

        context = self.get_context_data(form, formset)
        return render(request, self.template_name, context)

    def get(self, request, *args, **kwargs):
        estoque_form = Estoque()
        item_estoque_formset = self.get_item_estoque_formset()

        form = EstoqueForm(instance=estoque_form, prefix="main")
        formset = item_estoque_formset(instance=estoque_form, prefix="estoque")

        context = self.get_context_data(form, formset)
        return render(request, self.template_name, context)

@method_decorator(login_required, name="dispatch")
class EstoqueEntradaAdd(EstoqueAdd):
    template_name = "estoque_entrada_form.html"
    movimento = "e"

@method_decorator(login_required, name='dispatch')
class EstoqueSaidaList(ListView):
    model = EstoqueSaida
    template_name = 'estoque_list.html'

    def get_queryset(self):
        return EstoqueSaida.objects.all().order_by('-created')

    def get_context_data(self, **kwargs):
        context = super(EstoqueSaidaList, self).get_context_data(**kwargs)
        context['titulo'] = 'Saída'
        context['url_add'] = 'estoque:estoque_saida_add'
        return context


@method_decorator(login_required, name="dispatch")
class EstoqueSaidaAdd(EstoqueAdd):
    template_name = "estoque_saida_form.html"
    movimento = "s"