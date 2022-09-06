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
            fechaNac=carga["fechaNac_aaaa_mm_dd"]
            dni=carga["dni"]
            tel=carga["tel"]
            email=carga["email"]
            newSocio=Socio(nombre=nombre, apellido=apellido, fechaNac=fechaNac, dni=dni, tel=tel, email=email)
            newSocio.save()
            return render (request, "Appclub/cargaExitosa.html")
    else:
        formulario=FormSocio()
        return render (request, "Appclub/cargaSocio.html", { "formulario":formulario})
    
def profe(request):
    if request.method=="POST":
        profe=FormProfesor(request.POST)
        if profe.is_valid():
            carga=profe.cleaned_data
            nombre=carga["nombre"]
            apellido=carga["apellido"]
            email=carga["email"]
            tel=carga["tel"]
            disciplina=carga["disciplina"]
            newProfe=Profesor(nombre=nombre, apellido=apellido, email=email, tel=tel, disciplina=disciplina)
            newProfe.save()
            return render (request, "Appclub/cargaExitosa.html")
    else:
        formulario=FormProfesor()
        return render (request, "Appclub/cargaProfe.html", { "formulario":formulario}) 
    
def disciplina(request):
    if request.method=="POST":
        disc=FormDisciplina(request.POST)
        if disc.is_valid():
            carga=disc.cleaned_data
            nombre=carga["nombre"]
            categoria=carga["categoria"]
            newDisc=Disciplina(nombre=nombre, categoria=categoria)
            newDisc.save()
            return render (request, "Appclub/cargaExitosa.html")
    else:
        formulario=FormDisciplina()
        return render (request, "Appclub/cargaDisciplina.html", { "formulario":formulario})
            
