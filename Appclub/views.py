from django.shortcuts import render

# Create your views here.

def inicioApp(request):
    return render (request, "Appclub/index.html")