from django.urls import path
from Appclub.views import *


urlpatterns = [
    path('', inicio, name="inicio"),
    path("cargaSocio", socio, name="socio"),
    path("cargaProfe", profe, name="profe"),
    path("cargaDisciplina", disciplina, name="disciplina")
]
