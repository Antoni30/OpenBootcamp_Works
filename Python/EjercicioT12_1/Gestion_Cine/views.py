from django.shortcuts import render
from django.views.generic import ListView
from .models import Director,Peliculas

class home(ListView):
    template_name = 'home.html'
    model = Director
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Cine"
        return context
    
# Create your views here.
