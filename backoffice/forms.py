from django.forms import ModelForm

from backoffice.models import *


class PaisForm(ModelForm):
    class Meta:
        model = Pais
        fields = ['nombre',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre', 'pais',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class ProvinciaForm(ModelForm):
    class Meta:
        model = Provincia
        fields = ['nombre', 'departamento', 'pais',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class DistritoForm(ModelForm):
    class Meta:
        model = Distrito
        fields = ['nombre', 'provincia', 'departamento', 'pais',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class EstacionamientoForm(ModelForm):
    class Meta:
        model = Estacionamiento
        fields = ['nombre', 'direccion', 'distrito', 'provincia', 'departamento', 'pais', 'telefono', 'costo', 'latitud', 'longitud',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})