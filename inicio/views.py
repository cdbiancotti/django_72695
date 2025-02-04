from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    # return HttpResponse("<h1>ESTE ES MI PRIMERA VISTA</h1>")
    return render(request, 'inicio/inicio.html')