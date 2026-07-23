from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('dishes/<str:dish>', views.menu, name='dishes'),
    re_path(r'^dishes/([0-9]{2})/$', views.menu)
]
'''
^: Se utiliza para anclar el comienzo de la cadena
$: Se utiliza como ancla para el final de la cadena
[0-9]: Coincide con cualquiera de lo que esta en el interior
{2}: Especificar el nnumero exacto de caracteres anteriores
(): Dentro se agrupan ek regex
'''