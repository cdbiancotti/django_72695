from django.urls import path
from inicio.views import inicio, crear_auto, listar_autos

urlpatterns = [
    path('', inicio, name="inicio"),
    path('crear-auto/', crear_auto, name="crear_auto"),
    path('listar-autos/', listar_autos, name="listar_autos"),
]
