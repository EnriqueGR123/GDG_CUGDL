from rest_framework import routers
from .api import ProjectViewSet



#Enrutador por defecto, es el que se va a encargar de manejar las rutas de la API
router = routers.DefaultRouter()
router .register('api/projects/', ProjectViewSet, basename='projects')
urlpatterns = router.urls
