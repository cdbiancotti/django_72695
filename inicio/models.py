from django.db import models


class Auto(models.Model):
    modelo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    descripcion = models.TextField(null=True, blank=True)
    # campo_imagen: Queda para uds
    fecha_creacion = models.DateField(null=True)
    
    def __str__(self):
        return f'{self.marca} {self.modelo}'
