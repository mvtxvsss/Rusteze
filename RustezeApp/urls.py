from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('',views.Index,  name='Index'),
    #path('',views.Base,  name='Base'),
    path('Tienda',views.Tienda,  name='Tienda'),
    path('SobreNosotros',views.SobreNosotros,  name='SobreNosotros'),
    path('Contacto',views.Contacto,  name='Contacto'),
    path('IniciarSesion',views.IniciarSesion,  name='IniciarSesion'),
    path('Registro',views.Resgistro,  name='Registro'),
    path('ListarProductos',views.listar_productos,  name='ListarProductos'),
    path('Agregar', views.agregar_producto , name="AgregarProducto" ),
]
