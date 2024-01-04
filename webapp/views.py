from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from estudiantes.models import Estudiante


# Create your views here.

def bienvenido(request):
    cantidad_estudiantes=Estudiante.objects.count()
    estudiantes=Estudiante.objects.order_by('apellido','nombre')
    dict_datos={'cantidad_estudiantes':cantidad_estudiantes,'personas':estudiantes}
    pagina=loader.get_template('bienvenida.html')
    return HttpResponse(pagina.render(dict_datos,request))