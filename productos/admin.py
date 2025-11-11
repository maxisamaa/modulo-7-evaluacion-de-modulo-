from django.contrib import admin
from .models import Producto, Detalles
from etiquetas.models import Etiqueta

class DetallesInline(admin.StackedInline):
    model = Detalles
    extra = 0

class EtiquetaInline(admin.TabularInline):
    model = Etiqueta.productos.through  # usa la tabla intermedia del ManyToMany
    extra = 1

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('categoria',)
    inlines = [DetallesInline, EtiquetaInline]

    # evita mostrar el campo intermedio duplicado
    exclude = ('etiquetas',)

# Registro normal de Detalles
admin.site.register(Detalles)
