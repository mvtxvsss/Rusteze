from django.shortcuts import render, redirect
from sweetify import success, warning, error
from django.contrib.auth import logout  # authenticate, login
from .form import *
# from django.http import HttpResponse


def base(request):
    return render(request, 'base/base.html')


def index(request):
    return render(request, 'index.html')


def tienda(request):
    return render(request, 'Tienda.html')


def sobre_nosotros(request):
    return render(request, 'sobrenosotros.html')


def contacto(request):
    return render(request, 'Contacto.html')


def iniciar_sesion(request):
    return render(request, 'login.html')


def resgistro(request):
    return render(request, 'registro.html')


def listar_productos(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'listar_productos.html', context)


def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(initial={'prod_id': 0})
        if form.is_valid():
            form.save()
            success(request, 'El producto se ha agreado correctamente!')
            return redirect('ListarProductos')
    else:
        form = ProductoForm()

    return render(request, 'agregar_producto.html', {'form': form})


def mostrar_registro(request):
    if request.method == 'GET':
        contexto = {
            'formulario': Registro()
        }
        return render(request, 'registro_test.html', contexto)
    if request.method == 'POST':
        formulario_registro = Registro(data=request.POST)
        es_valido = formulario_registro.is_valid()
        if es_valido:
            print('Valido')
            usuario_nuevo = formulario_registro.save()
            success(request, 'Se ha registrado su cuenta')
            return redirect('Index')
        contexto = {
            'formulario': formulario_registro
        }
        error(request, 'A ocurrido un error, vuelva a intentarlo.')
        return render(request, 'registro_test.html', contexto)


def cerrar_sesion(request):
    if request.user.is_authenticated:
        logout(request)
        warning(request, 'Se cerro la sesión')
    return redirect('Index')
