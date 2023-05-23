from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
#from .models import RustezeApp

def Index(request):

    
    return render(request,'index.html')
