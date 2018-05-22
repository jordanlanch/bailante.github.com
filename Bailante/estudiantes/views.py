from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

# Create your views here.

class HomeView(TemplateView):
    template_name = 'estudiantes/index.html'

    """def get_context_data(self, *args, **kwargs):
        estudiantes = Product.objects.all()
        return {'products': products}"""
