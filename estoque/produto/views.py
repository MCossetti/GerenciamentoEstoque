from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView, DeleteView
from .models import Produto, Categoria
from .forms import ProdutoForm, CategoriaForm

class ProdutoList(ListView):
    model = Produto
    template_name = 'produto_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(nome__icontains=search)
        return queryset

class ProdutoDetail(DetailView):
    model = Produto
    template_name = 'produto_detail.html'
    context_object_name = 'object'


class ProdutoAddView(TemplateView):
    template_name = 'produto_form.html'

class ProdutoCreate(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm

class ProdutoUpdate(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm

class ProdutoJson(View):
    def get(self, request, pk, *args, **kwargs):
        produto = Produto.objects.filter(pk=pk)
        data = [item.to_dict_json() for item in produto]
        return JsonResponse({'data': data})
    
class ProdutoDelete(DeleteView):
    model = Produto
    success_url = reverse_lazy('produto:produto_list') 
    
class CategoriaCreate(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria_form.html'
    success_url = reverse_lazy('produto:categoria_list')

class CategoriaList(ListView):
    model = Categoria
    template_name = 'categoria_list.html'
    context_object_name = 'categorias'

    def categoria_list(request):
        categorias = Categoria.objects.all()
        return render(request, 'produto/categoria_list.html', {'categorias': categorias})
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(nome__icontains=search)
        return queryset

class CategoriaEdit(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria_form.html'
    success_url = reverse_lazy('produto:categoria_list')

class CategoriaDelete(DeleteView):
    def post(self, request, pk):
        categoria = get_object_or_404(Categoria, pk=pk)
        categoria.delete()
        return redirect('produto:categoria_list')