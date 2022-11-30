from rest_framework import serializers
from .models import Profesor,Agenda,Alumno,Asignatura,Asistencia,Forma,Pago,Plataforma

class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '_all_'
        read_only_fields = ('fechacreacion',)

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '_all_'
        read_only_fields = ('fechacreacion',)

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = '_all_'
        read_only_fields = ('fechaAsistencia',)
        
class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '_all_'
        read_only_fields = ('fechacreacion',)

class PlataformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plataforma
        fields = '_all_'
        read_only_fields = ('fechacreacion',)

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = '_all_'

class FormaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forma
        fields = '_all_'
        read_only_fields = ('fechacreacion',)

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '_all_'
        read_only_fields = ('fechaPago',)