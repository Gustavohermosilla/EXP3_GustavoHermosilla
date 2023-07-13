from django.urls import path
from .views import principal, productos, quiensomos, feriados,almacen,crear,eliminar,modificar,registrar,mostrar,tienda,carrito,generarBoleta,agregar_producto,eliminar_producto,restar_producto,limpiar_carrito

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
    path('tienda/',tienda, name="tienda"),
    path('carrito/',carrito, name="carrito"),
    path('generarBoleta/', generarBoleta,name="generarBoleta"),
    path('agregar/<id>', agregar_producto, name="agregar"),
    path('eliminar/<id>', eliminar_producto, name="eliminar"),
    path('restar/<id>', restar_producto, name="restar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
]