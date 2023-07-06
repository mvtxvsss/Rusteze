from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', views.index, name='Index'),
    path('SobreNosotros', views.sobre_nosotros, name='SobreNosotros'),
    path('Contacto', views.contacto, name='Contacto'),
    path('IniciarSesion', views.user_login, name='IniciarSesion'),
    path('Registro', views.mostrar_registro, name='Registro'),
    # path('ListarProductos', views.listar_productos, name='ListarProductos'),
    # path('Agregar', views.agregar_producto, name='AgregarProducto'),
    path('user_login', views.user_login, name='user_login'),
    path('register', views.mostrar_registro, name='register'),
    path('cerrar', views.cerrar_sesion, name='CerrarSesion'),


    # Tienda usuarios
    path('tienda', views.tienda_publica, name='tienda'),
    path('carrito', views.mostrar_carrito, name='carrito'),

    # Carrito
    path('agregar_carrito/<id>', views.agregar_carrito, name='agregar_carrito'),
    path('quitar/<id>', views.quitar_producto_carrito, name='quitar'),
    path('vaciar', views.vaciar_carrito, name='vaciar'),
    path('incrementar/<id>', views.incrementar_producto_carrito, name='incrementar'),
    path('decrementar/<id>', views.decrementar_producto_carrito, name='decrementar'),

    # Urls tienda
    path('Tienda', views.tienda, name='Tienda'),
    path('Mantenedor', views.mantenedor, name='Mantenedor'),
    path('Agregar', views.agregar, name="Agregar"),
    path('Modificar/<id>', views.modificar, name="Modificar"),
    path('Eliminar/<id>', views.eliminar, name="Eliminar"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
