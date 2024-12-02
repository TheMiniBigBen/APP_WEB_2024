from django import forms
from .models import Cliente, Direccion
from django.db import models

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido_paterno', 'apellido_materno', 'telefono', 'correo']

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['calle', 'colonia', 'numero', 'codigo_postal']
        labels = {
            'calle': 'Calle',
            'colonia': 'Colonia',
            'numero': 'Número de Casa',
            'codigo_postal': 'Código Postal',
        }