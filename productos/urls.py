from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', lista_productos.as_view(), name='producto-lista'),
    path('productos/crear/', crear_producto.as_view(), name='crear_producto'),
    path('productos/<int:pk>/', detalle_producto.as_view(), name='detalle_producto'),
    path('productos/<int:pk>/editar/', editar_producto.as_view(), name='editar_producto'),
    path('productos/<int:pk>/eliminar/', eliminar_producto.as_view(), name='eliminar_producto'),
]