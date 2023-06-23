from RustezeApp.models import Producto
from django.shortcuts import render, redirect
#from form import ProductoForm
from sweetify import info, success, warning, error
from .form import ProductoForm

def Base(request):

    return render(request,'base.html')
def Index(request):

    return render(request,'index.html')

def Tienda(request):

    return render(request,'Tienda.html')

def SobreNosotros(request):

    return render(request,'sobrenosotros.html')

def Contacto(request):

    return render(request,'Contacto.html')

def IniciarSesion(request):

    return render(request,'login.html')

def Resgistro(request):

    return render(request,'registro.html')

def listar_productos(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'listar_productos.html', context)



def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(initial={'prod_id': 0})
        if form.is_valid():
            form.save()
            success(request,'El producto se ha agreado correctamente!')
            return redirect('ListarProductos')
    else:
        form = ProductoForm()
    
    return render(request,'agregar_producto.html',{'form':form})


"""
def agregar_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            gato = form.save(commit=False)
            form.save()
        alumnos = Producto.objects.all()
        return render(request,'paginab.html', {'alumnos':alumnos})
    else:
        form = ProductoForm()
        return render(request,'agregarAlumno.html',{'form':form})

"""