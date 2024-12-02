from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('estoque.core.urls')),
    path('produto/', include('estoque.produto.urls')),
    path('estoque/', include('estoque.stock.urls')),
    path('account/', include('estoque.account.urls')),
]

# rota pra imagem que não estava indo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)