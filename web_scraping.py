import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver


def cambiar_caracter(texto):
    return texto.replace('Ñ', 'N')

driver = webdriver.Chrome()
driver.get('http://127.0.0.1:8000/lista_estudiantes/')
html_pagina = driver.page_source
contenido = BeautifulSoup(html_pagina, 'html.parser')

# Modify the following part based on the actual structure of the webpage
datos = contenido.find('table')
nombres = []
edades = []
notas = []

if datos:
    filas_tabla = datos.find_all('tr')
    for fila in filas_tabla[1:]:
        celdas = fila.find_all('td')
        nombres.append(cambiar_caracter(celdas[0].text.strip()))
        edades.append(cambiar_caracter(celdas[1].text.strip()))
        notas.append(cambiar_caracter(celdas[2].text.strip()))

dataframe_estudiantes = pd.DataFrame({
    'Nombre': nombres,
    'Edad': edades,
    'Nota': notas
})

dataframe_estudiantes.to_csv('datosEstudiantes.csv', index=False, encoding='utf-8-sig')


def cambiar_caracter(texto):
    return texto.replace('Ñ', 'N')

driver = webdriver.Chrome()
driver.get('http://127.0.0.1:8000/lista_cursos/')
html_pagina = driver.page_source
contenido = BeautifulSoup(html_pagina, 'html.parser')

# Modify the following part based on the actual structure of the webpage
datos = contenido.find('table')
nombres = []


if datos:
    filas_tabla = datos.find_all('tr')
    for fila in filas_tabla[1:]:
        celdas = fila.find_all('td')
        nombres.append(cambiar_caracter(celdas[0].text.strip()))

dataframe_cursos = pd.DataFrame({
    'Nombre del Curso': nombres,
})

dataframe_cursos.to_csv('datosCursos.csv', index=False, encoding='utf-8-sig')


def cambiar_caracter(texto):
    return texto.replace('Ñ', 'N')

driver = webdriver.Chrome()
driver.get('http://127.0.0.1:8000/lista_calificaciones/')
html_pagina = driver.page_source
contenido = BeautifulSoup(html_pagina, 'html.parser')

# Modify the following part based on the actual structure of the webpage
datos = contenido.find('table')
nombres_estudiantes = []
calificaciones = []

if datos:
    filas_tabla = datos.find_all('tr')
    for fila in filas_tabla[1:]:
        celdas = fila.find_all('td')
        nombres_estudiantes.append(cambiar_caracter(celdas[0].text.strip()))
        calificaciones.append(cambiar_caracter(celdas[1].text.strip()))

dataframe_calificaciones = pd.DataFrame({
    'Nombre del Estudiante': nombres_estudiantes,
    'Calificación': calificaciones
})

dataframe_calificaciones.to_csv('datosCalificaciones.csv', index=False, encoding='utf-8-sig')
driver.quit()
