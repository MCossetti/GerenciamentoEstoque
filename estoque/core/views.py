from django.shortcuts import redirect, render
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  
        return render(request, 'index.html')