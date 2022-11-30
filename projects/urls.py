from rest_framework import routers
from .api import AgendaViewSet,AlumnoViewSet,AsignaturaViewSet,AsistenciaViewSet,FormaViewSet,PagoViewSet,PlataformaViewSet,ProfesorViewSet

router = routers.DefaultRouter()

router.register('api/Agenda', AgendaViewSet, 'Agenda')
router.register('api/Alumno', AlumnoViewSet, 'Alumno')
router.register('api/Asignatura', AsignaturaViewSet, 'Asignatura')
router.register('api/Asistencia', AsistenciaViewSet, 'Asistencia')
router.register('api/Forma', FormaViewSet, 'Forma')
router.register('api/Pago', PagoViewSet, 'Pago')
router.register('api/Plataforma', PlataformaViewSet, 'Plataforma')
router.register('api/Profesor', ProfesorViewSet, 'Profesor')

urlpatterns = router.urls
