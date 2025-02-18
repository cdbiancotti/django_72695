from django import forms

class CrearAuto(forms.Form):
    modelo = forms.CharField(max_length=20)
    marca = forms.CharField(max_length=20)
    descripcion = forms.CharField(required=False, widget=forms.Textarea)
    
    
class BuscarAutos(forms.Form):
    modelo = forms.CharField(max_length=20, required=False)