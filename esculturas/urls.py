from django.urls import path
from .views import principal, productos, quiensomos, feriados,almacen,crear,eliminar,modificar,registrar,mostrar

urlpatterns=[ 
    path('',principal, name="principal"),
    path('productos/',productos, name='productos'),
    path('quiensomos/',quiensomos, name='quiensomos'),
    path('feriados/',feriados, name='feriados'),
    path('almacen/',almacen, name="almacen"),
    path('crear/', crear, name="crear"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('modificar/<id>', modificar, name="modificar"),
    path('registrar/', registrar, name="registrar"),
    path('mostrar/', mostrar,name="mostrar"),
]