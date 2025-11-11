from django import forms
from .models import Producto
from etiquetas.models import Etiqueta

class ProductoForm(forms.ModelForm):
    etiquetas = forms.ModelMultipleChoiceField(
        queryset=Etiqueta.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Etiquetas"
    )
    peso = forms.DecimalField(max_digits=6, decimal_places=2)
    alto = forms.DecimalField(max_digits=5, decimal_places=2)
    largo = forms.DecimalField(max_digits=5, decimal_places=2)
    ancho = forms.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'categoria', 'peso', 'alto', 'largo', 'ancho']
