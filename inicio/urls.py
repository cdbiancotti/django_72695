from django.urls import path
from inicio.views import inicio, crear_auto, listar_autos, detalle_auto, borrar_auto

urlpatterns = [
    path('', inicio, name="inicio"),
    path('crear-auto/', crear_auto, name="crear_auto"),
    path('listar-autos/', listar_autos, name="listar_autos"),
    path('ver-auto/<int:id>/', detalle_auto, name="detalle_auto"),
    path('borrar-auto/<int:id>/', borrar_auto, name="borrar_auto"),
]
