from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Categoria, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUserForm(UserCreationForm):
    class Meta:
        model= User
        fields = ['username', 'first_name', 'last_name', 'email','password1', 'password2']

class EsculturasForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['idproducto', 'producto', 'precio','stock', 'imagen', 'categoria']
        labels = {
            'idproducto': 'Idproducto',
            'producto': 'Producto',
            'precio': 'Precio',
            'stock' : 'Stock',
            'imagen': 'Imagen',
            'categoria': 'Categoria'
        }
        widgets = {
            'idproducto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese Idproducto..',
                    'id': 'codigo',
                }
            ),
            'producto':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese nombre..',
                    'id': 'marca',
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese precio..',
                    'id': 'precio',
                }
            ),
            'stock': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese stock..',
                    'id': 'stock',
                }
            ),
            'imagen':forms.FileInput(
                attrs={
                    'id': 'imagen',
                    'class': 'form-control',
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id':'categoria',
                }
            )

        }