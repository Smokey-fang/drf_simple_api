from .models import Project
from rest_framework import viewsets, permissions
from .serializer import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer