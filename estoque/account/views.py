from django.shortcuts import redirect, request, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.messages import messages
from django.http import HttpResponseRedirect

def admin_login(resquest):
    try:
        if request.user.is_authenticated:
            return redirect('core:index')
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username = username)
            if not user_obj.exists():
                messages.info(request, 'Conta não encontrada')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
            user_obj = authenticate(username = username, password = password)

            if user_obj and user_obj.is_superuser:
                login(request, user_obj)
                return redirect('core:index')
            
            messages.info(request, 'Senha invalida')
            return redirect('')
        return render (request, 'login.html')
    
    except Exception as e:
        print(e)