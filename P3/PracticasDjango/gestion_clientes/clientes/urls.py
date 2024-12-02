from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('<int:cliente_id>/direccion/', views.ver_direcciones, name='ver_direcciones'),
    path('<int:cliente_id>/direccion/agregar/', views.agregar_direccion, name='agregar_direccion'),
    path('<int:cliente_id>/direccion/<int:direccion_id>/editar/', views.editar_direccion, name='editar_direccion'),  # Añadido para editar
    path('<int:cliente_id>/direccion/<int:direccion_id>/eliminar/', views.eliminar_direccion, name='eliminar_direccion'),  # Añadido para eliminar
    path('<int:cliente_id>/editar/', views.editar_cliente, name='editar_cliente'),
    path('<int:cliente_id>/eliminar/', views.eliminar_cliente, name='eliminar_cliente'),
]