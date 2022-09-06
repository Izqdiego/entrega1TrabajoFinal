from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from Appclub.forms import *

# Create your views here.

def inicio(request):
    return render (request, "Appclub/inicio.html")

def socio(request):
    if request.method=="POST":
    
        socio=FormSocio(request.POST)
        if socio.is_valid():
            carga=socio.cleaned_data
            nombre=carga["nombre"]
            apellido=carga["apellido"]
            fechaNac=carga["fechaNac"]
            dni=carga["dni"]
            tel=carga["tel"]
            email=carga["email"]
            newSocio=Socio(nombre=nombre, apellido=apellido, fechaNac=fechaNac, dni=dni, tel=tel, email=email)
            newSocio.save()
            return render (request, "Appclub/inicio.html")
    else:
        formulario=FormSocio()
        return render (request, "Appclub/cargaSocio.html", { "formulario":formulario})

