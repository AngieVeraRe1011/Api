from django.contrib import admin

# Register your models here.
from .models import Estudiante, Curso, Calificaciones

admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Calificaciones)