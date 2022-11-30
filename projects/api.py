from .models import Profesor,Agenda,Alumno,Asignatura,Asistencia,Forma,Pago,Plataforma
from rest_framework import viewsets, permissions
from .serializer import AgendaSerializer,AlumnoSerializer,AsignaturaSerializer,AsistenciaSerializer,FormaSerializer,PagoSerializer,PlataformaSerializer,ProfesorSerializer

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProfesorSerializer

class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AgendaSerializer

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AlumnoSerializer

class AsignaturaViewSet(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AsignaturaSerializer

class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AsistenciaSerializer

class FormaViewSet(viewsets.ModelViewSet):
    queryset = Forma.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FormaSerializer

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PagoSerializer

class PlataformaViewSet(viewsets.ModelViewSet):
    queryset = Plataforma.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PlataformaSerializer