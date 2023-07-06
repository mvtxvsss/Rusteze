from django.shortcuts import render, redirect, get_object_or_404
from sweetify import success, warning, error
from django.contrib.auth import logout, authenticate, login
from .form import *
from django.contrib.auth.decorators import user_passes_test
from .cart import *


def base(request):
    return render(request, 'base/base.html')


def index(request):
    return render(request, 'index.html')


def tienda(request):
    productos = Producto.objects.all()
    return render(request, 'tienda.html', {'productos': productos})


def tienda_publica(request):
    productos = Producto.objects.all()
    return render(request, 'tienda_publica.html', {'productos': productos})


def carrito(request):
    return render(request, 'carrito.html')


def sobre_nosotros(request):
    return render(request, 'sobrenosotros.html')


def contacto(request):
    return render(request, 'contacto.html')


def validate_user(user):
    return user.is_authenticated and user.is_staff


@user_passes_test(validate_user)
def mantenedor(request):
    return render(request, 'mantenedor.html')


def iniciar_sesion(request):
    return render(request, 'login.html')


def agregar_carrito(request, id):
    cart = Cart(request)
    producto = get_object_or_404(Producto, id=id)
    cart.add(producto)
    success(request, f'Se ha agregado {producto.nombre.lower()} al carrito')
    return redirect("tienda")


def mostrar_carrito(request):
    cart = Cart(request)
    context = {
        'cart': cart.get_products(),
        'subtotal': cart.get_subtotal_price(),
        'iva': cart.get_iva(),
        'total': cart.get_total_price()
    }
    return render(request, 'carrito.html', context)


def quitar_producto_carrito(request, id):
    cart = Cart(request)
    producto = get_object_or_404(Producto, id=id)
    cart.remove(producto)
    return redirect("carrito")


def vaciar_carrito(request):
    cart = Cart(request)
    cart.clear()
    return redirect("carrito")


def incrementar_producto_carrito(request, id):
    cart = Cart(request)
    producto = get_object_or_404(Producto, id=id)
    cart.increment(producto)
    return redirect("carrito")


def decrementar_producto_carrito(request, id):
    cart = Cart(request)
    producto = get_object_or_404(Producto, id=id)
    cart.decrement(producto)
    return redirect("carrito")


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
        return render(request, 'registro.html', contexto)
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
        return render(request, 'registro.html', contexto)


def cerrar_sesion(request):
    if request.user.is_authenticated:
        logout(request)
        warning(request, 'Se cerro la sesión')
    return redirect('Index')


def user_login(request):
    if request.method == 'POST':
        form = IniciarSesion(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            usuario = authenticate(request, username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                success(request, f'Se inició sesion, Bienvenido {username}')
                return redirect('Index')
            else:
                error(request, 'Nombre de usuario o contraseña incorrectos.')
    elif request.method == 'GET':
        return render(request, 'login.html')
    else:
        form = IniciarSesion()

    return render(request, 'login.html', {'form': form})


def agregar(request):
    data = {
        'form': ProductoForm
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            success(request, 'Se registro el producto!')
            return redirect(to="Tienda")
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'producto/agregar.html', data)


def modificar(request, id):
    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            success(request, 'Se modifico el producto!')
            return redirect(to="Tienda")
        data["form"] = formulario

    return render(request, 'producto/modificar.html', data)


def eliminar(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    success(request, 'Se elimino el producto.')
    return redirect(to="Tienda")
