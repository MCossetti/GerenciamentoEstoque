from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Produto
from .forms import ProdutoForm

class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(nome__icontains=search)
        return queryset

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto_detail.html'
    context_object_name = 'object'

class ProdutoAddView(View):
    template_name = 'produto_form.html'

    def get(self, request):
        """Renderiza o formulário de adição de produto."""
        form = ProdutoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        """Processa a criação de um novo produto."""
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Produto criado com sucesso.'})
        return render(request, self.template_name, {'form': form})

class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm

class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm

class ProdutoJsonView(View):
    def get(self, request, pk):
        """Retorna o produto, ID e estoque em formato JSON."""
        produto = get_object_or_404(Produto, pk=pk)
        data = {
            'id': produto.id,
            'nome': produto.nome,
            'estoque': produto.estoque,
        }
        return JsonResponse({'data': data})