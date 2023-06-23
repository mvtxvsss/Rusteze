from django import forms
from django.forms import fields
from .models import Producto
from django.shortcuts import render


class ProductoForm(forms.ModelForm):

    class Meta:
       model = Producto
       fields = [ 'nombre', 'descripcion','precio']
    #    widgets = {
    #         'nombre': forms.TextInput(
    #             attrs = {
    #                 'class':'form-control',
    #                 'placeholder':'Nombre del Producto'
    #             }
    #         ),
    #         'descripcion': forms.TextInput(
    #             attrs = {
    #                 'class':'form-control',
    #                 'placeholder':'Descripcion'
    #             }
    #         ),
    #         'precio': forms.NumberInput(
    #             attrs = {
    #                 'class':'form-control',
    #                 'placeholder':'Precio'
    #             }
    #         )
    #         }