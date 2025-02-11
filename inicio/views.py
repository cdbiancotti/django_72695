from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Auto
from inicio.forms import CrearAuto

def inicio(request):
    # return HttpResponse("<h1>ESTE ES MI PRIMERA VISTA</h1>")
    return render(request, 'inicio/inicio.html')

def crear_auto(request):
    # print(request.GET)
    # print(request.POST)
    formulario = CrearAuto()
    if request.method == "POST":
        formulario = CrearAuto(request.POST)
        if formulario.is_valid():
            print('Cleaned Data:', formulario.cleaned_data)
            modelo = formulario.cleaned_data.get('modelo')
            
            auto = Auto(
                modelo=modelo,
                marca=formulario.cleaned_data.get('marca'),
                descripcion=formulario.cleaned_data.get('descripcion')
            )
            auto.save()
            return redirect("listar_autos")
            
    return render(request, 'inicio/crear_auto.html', {'formulario': formulario})

def listar_autos(request):
    autos = Auto.objects.all()
    return render(request, 'inicio/listar_autos.html', {'autos': autos})