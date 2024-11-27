from django.urls import path
from estoque.produto import views as v

app_name = 'produto'

urlpatterns = [
    path('', v.ProdutoListView.as_view(), name='produto_list'),
    path('<int:pk>/', v.ProdutoDetailView.as_view(), name='produto_detail'),
    path('add/', v.ProdutoCreateView.as_view(), name='produto_add'),
    path('<int:pk>/edit/', v.ProdutoUpdateView.as_view(), name='produto_edit'),
    path('<int:pk>/json/', v.ProdutoJsonView.as_view(), name='produto_json'),
]