from django import forms
from inicio.models import Auto

class CrearAuto(forms.Form):
    modelo = forms.CharField(max_length=20)
    marca = forms.CharField(max_length=20)
    descripcion = forms.CharField(required=False, widget=forms.Textarea)
    fecha_creacion = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    
    
class BuscarAutos(forms.Form):
    modelo = forms.CharField(max_length=20, required=False)
    
    
class EditarAutoFormulario(forms.ModelForm):
    fecha_creacion = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Auto
        # fields = ['marca', 'modelo']
        fields = '__all__'