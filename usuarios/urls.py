from django.urls import path
from django.contrib.auth.views import LogoutView
from usuarios.views import login, registro, editar_perfil

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('registro/', registro, name='registro'),
    path('editar-perfil/', editar_perfil, name='editar_perfil'),
]
