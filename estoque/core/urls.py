from django.urls import path
from estoque.core import views as v

app_name = 'core'

urlpatterns=[
    path('', v.IndexView.as_view(), name='index')
]