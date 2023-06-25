from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index, name='Index'),
    path('Tienda', views.tienda, name='Tienda'),
    path('SobreNosotros', views.sobre_nosotros, name='SobreNosotros'),
    path('Contacto', views.contacto, name='Contacto'),
    path('IniciarSesion', views.LogIn, name='IniciarSesion'),
    path('Registro', views.resgistro, name='Registro'),
    path('ListarProductos', views.listar_productos, name='ListarProductos'),
    path('Agregar', views.agregar_producto, name='AgregarProducto'),
    #path('login', views.show_login, name='login'),
    path('register', views.mostrar_registro, name='register'),
    path('cerrar', views.cerrar_sesion, name='CerrarSesion'),
    path('mostrar_iniciar_sesion/', views.mostrar_iniciar_sesion, name='mostrar_iniciar_sesion'),
]
