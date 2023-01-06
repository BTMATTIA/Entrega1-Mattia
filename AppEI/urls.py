from django.urls import path
from .views import *


urlpatterns = [
    path('', inicio, name="inicio"),

    path('TerrorFormulario/', terrorFormulario, name="terrorFormulario"),
    path('ComediaFormulario/', comediaFormulario, name="comediaFormulario"),
    path('AccionFormulario/', accionFormulario, name="accionFormulario"),

    path('busquedaTerror/', busquedaTerror, name="busquedaTerror"),
    path('buscar/', buscar, name="buscar"),

    path('leerTerror/', leerTerror, name="leerTerror"),
    path('eliminarTerror/<id>', eliminarTerror, name="eliminarTerror"),
    path('editarTerror/<id>', editarTerror, name="editarTerror"),

    path('leerComedia/', leerComedia, name="leerComedia"),
    path('eliminarComedia/<id>', eliminarComedia, name="eliminarComedia"),
    path('editarComedia/<id>', editarComedia, name="editarComedia"),

    path('leerAccion/', leerAccion, name="leerAccion"),
    path('eliminarAccion/<id>', eliminarAccion, name="eliminarAccion"),
    path('editarAccion/<id>', editarAccion, name="editarAccion"),
    

]