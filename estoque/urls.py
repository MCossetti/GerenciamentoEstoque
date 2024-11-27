from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('estoque.core.urls')),
    path('produto/', include('estoque.produto.urls')),
    path('estoque/', include('estoque.stock.urls')),
    path('account/', include('estoque.account.urls')),
]