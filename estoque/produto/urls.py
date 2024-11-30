from django.urls import path
from estoque.produto import views as v

app_name = 'produto'

urlpatterns = [
    path('', v.ProdutoList.as_view(), name='produto_list'),
    path('<int:pk>/', v.ProdutoDetail.as_view(), name='produto_detail'),
    path('add/', v.ProdutoCreate.as_view(), name='produto_add'),
    path('<int:pk>/edit/', v.ProdutoUpdate.as_view(), name='produto_edit'),
    path('<int:pk>/json/', v.ProdutoJson.as_view(), name='produto_json'),
    path('<int:pk>/delete/', v.ProdutoDelete.as_view(), name='produto_delete'),   

    path('categorias/', v.CategoriaList.as_view(), name='categoria_list'),
    path('categorias/add/', v.CategoriaCreate.as_view(), name='categoria_add'),
    path('categorias/<int:pk>/edit/', v.CategoriaEdit.as_view(), name='categoria_edit'), 
    path('categorias/<int:pk>/delete/', v.CategoriaDelete.as_view(), name='categoria_delete'),     
]