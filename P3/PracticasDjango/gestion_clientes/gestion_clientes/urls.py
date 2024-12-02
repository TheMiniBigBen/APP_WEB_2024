from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from clientes.views import custom_404_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),  # Asegúrate de incluir las URLs de la aplicación clientes
]

handler404 = custom_404_view
