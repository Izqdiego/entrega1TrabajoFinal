from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from Appclub.forms import *

# INICIO
def inicio(request):
    return render (request, "Appclub/inicio.html")
# CARGA SOCIO
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
# CARGA PROFESOR
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
# CARGA DISCIPLINA
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
#BUSQUEDA DE SOCIO 
def buscaSocio(request):
    return render(request, "Appclub/buscaSocio.html")
def buscarSocio(request):
    if not(request.GET["dni"]):
        return render(request, "Appclub/resBusSocio.html",)
    else:
        dni=request.GET["dni"]
        documentos=Socio.objects.filter(dni=dni)
        return render(request, "Appclub/resBusSocio.html", {"documentos":documentos})
# BUSQUEDA DE PROFESOR
def buscaProfe(request):
    return render (request, "Appclub/buscaProfe.html")
def buscarProfe(request):
    if not(request.GET["apellido"]):
        return render(request, "Appclub/resBusProfe.html",)
    else:
        apellido=request.GET["apellido"]
        apellidos=Profesor.objects.filter(apellido=apellido)
        return render(request, "Appclub/resBusProfe.html", {"apellidos":apellidos})
# BUSQUEDA DISCIPLINA
def buscaDisciplina(request):
    return render (request,"Appclub/buscaDisciplina.html")
def buscarDisciplina(request):
    if not(request.GET["nombre"]):
        return render(request, "Appclub/resBusDisc.html",)
    else:
        nombre=request.GET["nombre"]
        nombres=Disciplina.objects.filter(nombre=nombre)
        return render(request, "Appclub/resBusDisc.html", {"nombres":nombres})