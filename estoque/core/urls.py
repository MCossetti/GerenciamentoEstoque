from django.urls import path
from estoque.core import views as v
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

app_name = 'core'

@login_required(login_url='account/login/')
def index_redirect(request):
    return redirect('/produto')


urlpatterns=[
    path('', index_redirect, name='index'),
]