from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

#Que consultas se pueden hacer a la base de datos

class ProjectViewSet(viewsets.ModelViewSet): 
    queryset = Project.objects.all() # Conjntp de datos   
    permission_classes = [permissions.AllowAny] # Permisos de acceso
    serializer_class = ProjectSerializer