from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Producto, Cliente


class ProductoForm(ModelForm):
    class Meta: 
        model = Producto
        fields = ['codigo', 'precio', 'marca', 'nombre']        



class ClienteForm(forms.ModelForm):

    class Meta: 
        model= Cliente
        fields = ['nombre', 'apellido', 'rut', 'correo', 'telefono', 'direccion']
        labels ={
            'nombre': 'Nombre cliente', 
            'apellido': 'Apellido Cliente', 
            'rut': 'rut', 
            'correo': 'correo electrónico', 
            'telefono': 'Numero de telefono',
            'direccion': 'Dirección',
        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese apellido', 
                    'id': 'apellido',

                }
            ), 
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut', 
                    'id': 'rut'
                }
            ),
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese correo', 
                    'id': 'correo'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese numero de telefono', 
                    'id': 'telefono',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese direccion', 
                    'id': 'direccion',
                }
            )
        }