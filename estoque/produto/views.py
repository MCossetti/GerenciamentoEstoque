from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from .models import Produto
from .forms import ProdutoForm

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