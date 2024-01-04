from rest_framework import serializers
from .models import Estudiante, Curso, Calificaciones

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ['id', 'nombre', 'apellido', 'correo']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nombre']

class CalificacionesSerializer(serializers.ModelSerializer):
    estudiante = EstudianteSerializer()
    curso = CursoSerializer()

    class Meta:
        model = Calificaciones
        fields = ['id', 'estudiante', 'curso', 'calificacion']

    def create(self, validated_data):
        estudiante_data = validated_data.pop('estudiante')
        curso_data = validated_data.pop('curso')

        estudiante_instance = Estudiante.agregar(**estudiante_data)
        curso_instance = Curso.agregar(**curso_data)

        return Calificaciones.objects.create(estudiante=estudiante_instance, curso=curso_instance, **validated_data)

    def update(self, instance, validated_data):
        estudiante_data = validated_data.pop('estudiante', {})
        curso_data = validated_data.pop('curso', {})

        instance.calificacion = validated_data.get('calificacion', instance.calificacion)
        instance.save()

        if estudiante_data:
            instance.estudiante.modificar(**estudiante_data)

        if curso_data:
            instance.curso.modificar(**curso_data)

        return instance
