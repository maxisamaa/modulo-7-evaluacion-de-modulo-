from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView , CreateView ,UpdateView, DeleteView , DetailView
from django.urls import reverse_lazy
from .models import Producto, Detalles
from .forms import ProductoForm



def index(request):
    return render(request,'index.html')

class lista_productos(ListView):
    model = Producto
    template_name = 'lista.html'
    context_object_name = 'productos'

class crear_producto(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'formulario.html'
    success_url = reverse_lazy('producto-lista')

    def form_valid(self, form):
        producto = form.save(commit=False)
        producto.save()

        # Crear detalles
        Detalles.objects.create(
            producto=producto,
            peso=form.cleaned_data['peso'],
            alto=form.cleaned_data['alto'],
            largo=form.cleaned_data['largo'],
            ancho=form.cleaned_data['ancho']
        )

        # Guardar etiquetas (ya que la relación está en Etiqueta)
        etiquetas = form.cleaned_data['etiquetas']
        for etiqueta in etiquetas:
            etiqueta.productos.add(producto)

        return redirect(self.success_url)


from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .models import Producto, Detalles
from .forms import ProductoForm

class editar_producto(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'formulario.html'
    success_url = reverse_lazy('producto-lista')

    def get_initial(self):
        initial = super().get_initial()
        producto = self.get_object()

        # Pre-cargar los detalles asociados (si existen)
        try:
            detalles = producto.detalles
            initial['peso'] = detalles.peso
            initial['alto'] = detalles.alto
            initial['largo'] = detalles.largo
            initial['ancho'] = detalles.ancho
        except Detalles.DoesNotExist:
            pass

        # Pre-cargar las etiquetas relacionadas
        initial['etiquetas'] = producto.etiquetas.all()

        return initial

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        # Guardar etiquetas seleccionadas
        form.save_m2m()

        # Actualizar o crear detalles
        detalles, _ = Detalles.objects.get_or_create(producto=self.object)
        detalles.peso = form.cleaned_data['peso']
        detalles.alto = form.cleaned_data['alto']
        detalles.largo = form.cleaned_data['largo']
        detalles.ancho = form.cleaned_data['ancho']
        detalles.save()

        return super().form_valid(form)


    
class eliminar_producto(DeleteView):
    model=Producto
    template_name='borrar.html' # para confirmar si borrar no mas  
    success_url=reverse_lazy('producto-lista') 

class detalle_producto(DetailView):
    model=Producto
    template_name='detalles.html'
    context_object_name='producto'
