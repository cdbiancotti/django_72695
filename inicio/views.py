from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Auto
from inicio.forms import CrearAuto, BuscarAutos, EditarAutoFormulario
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

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
                descripcion=formulario.cleaned_data.get('descripcion'),
                fecha_creacion=formulario.cleaned_data.get('fecha_creacion')
            )
            auto.save()
            return redirect("listar_autos")
            
    return render(request, 'inicio/crear_auto.html', {'formulario': formulario})

def listar_autos(request):
    
    formulario = BuscarAutos(request.GET)
    if formulario.is_valid():
        modelo = formulario.cleaned_data.get('modelo')
        autos = Auto.objects.filter(modelo__icontains=modelo)
    
    return render(request, 'inicio/listar_autos.html', {'autos': autos, 'formulario': formulario})

def detalle_auto(request, id):
    auto = Auto.objects.get(id=id)
    return render(request, 'inicio/detalle_auto.html', {'auto': auto})

def borrar_auto(request, id):
    auto = Auto.objects.get(id=id)
    auto.delete()
    return redirect("listar_autos")

class EditarAuto(LoginRequiredMixin, UpdateView):
    model = Auto
    template_name = "inicio/editar_auto.html"
    success_url = reverse_lazy("listar_autos")
    # fields = '__all__'
    form_class = EditarAutoFormulario
    
class BorrarAuto(LoginRequiredMixin, DeleteView):
    model = Auto
    template_name = "inicio/borrar_auto.html"
    success_url = reverse_lazy("listar_autos")
