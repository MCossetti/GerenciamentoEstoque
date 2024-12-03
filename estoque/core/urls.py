from django.urls import path
from estoque.core import views as v
from django.views.generic.base import RedirectView

app_name = 'core'

urlpatterns=[
    path('', RedirectView.as_view(url='produto', permanent=False), name='index')
]