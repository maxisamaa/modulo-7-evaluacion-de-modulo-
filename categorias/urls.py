from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('categorias/', lista_categorias.as_view(), name='lista_categorias'),
    path('categorias/crear/',crear_categoria.as_view(), name='crear_categoria'),
    path('categorias/editar/<int:pk>/', editar_categoria.as_view(), name='editar_categoria'),
    path('categorias/eliminar/<int:pk>/', eliminar_categoria.as_view(), name='eliminar_categoria'),
]

