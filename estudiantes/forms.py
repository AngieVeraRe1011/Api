# forms.py

from django import forms
from .models import Estudiante, Curso, Calificaciones

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'correo']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre']

class CalificacionesForm(forms.ModelForm):
    class Meta:
        model = Calificaciones
        fields = ['estudiante', 'curso', 'calificacion']
