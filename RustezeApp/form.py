from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio']


class Registro(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs = {'class': 'form-control'}
        self.fields['password2'].widget.attrs = {'class': 'form-control'}

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class IniciarSesion(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Nombre de Usuario'
        }
    ))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña'
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'password']

