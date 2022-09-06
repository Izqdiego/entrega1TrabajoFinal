from django.urls import path
from Appclub.views import *


urlpatterns = [
    path('', inicio, name="inicio"),
    path("cargaSocio", socio, name="socio"),
    path("cargaProfe", profe, name="profe"),
    path("cargaDisciplina", disciplina, name="disciplina"),
    path("buscaSocio", buscaSocio, name="buscaSocio"),
    path("resBusSocio", buscarSocio, name="buscarSocio"),
    path("buscaProfe", buscaProfe, name="buscaProfe"),
    path("resBusProfe", buscarProfe, name="buscarProfe"),
]
