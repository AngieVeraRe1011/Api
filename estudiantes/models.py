# models.py

from django.db import models

class Estudiante(models.Model):

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    @classmethod
    def agregar(cls, nombre, apellido, correo):
        return cls.objects.create(nombre=nombre, apellido=apellido, correo=correo)

    def modificar(self, nombre=None, apellido=None, correo=None):
        if nombre:
            self.nombre = nombre
        if apellido:
            self.apellido = apellido
        if correo:
            self.correo = correo
        self.save()

    def eliminar(self):
        self.delete()

    @classmethod
    def ver_todos(cls):
        return cls.objects.all()


class Curso(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    @classmethod
    def agregar(cls, nombre):
        return cls.objects.create(nombre=nombre)

    def modificar(self, nombre=None):
        if nombre:
            self.nombre = nombre
        self.save()

    def eliminar(self):
        self.delete()

    @classmethod
    def ver_todos(cls):
        return cls.objects.all()


class Calificaciones(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    calificacion = models.IntegerField()

    def __str__(self):
        return f"{self.estudiante} - {self.curso} - Calificación: {self.calificacion}"

    @classmethod
    def agregar(cls, estudiante, curso, calificacion):
        return cls.objects.create(estudiante=estudiante, curso=curso, calificacion=calificacion)

    def modificar(self, calificacion):
        self.calificacion = calificacion
        self.save()

    def eliminar(self):
        self.delete()

    @classmethod
    def ver_todas(cls):
        return cls.objects.all()
