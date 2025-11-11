
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Categoria

class lista_categorias(ListView):
    model = Categoria
    template_name = 'lista1.html'
    context_object_name = 'categorias'

class crear_categoria(CreateView):
    model = Categoria
    template_name = 'formulario1.html'
    fields = ['tipo']
    success_url = reverse_lazy('lista_categorias')

class editar_categoria(UpdateView):
    model = Categoria
    template_name = 'formulario1.html'
    fields = ['tipo']
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('lista_categorias')

class eliminar_categoria(DeleteView):
    model = Categoria
    template_name = 'borrar.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('lista_categorias')
