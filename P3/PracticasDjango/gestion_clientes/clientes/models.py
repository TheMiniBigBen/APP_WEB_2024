from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno}"

class Direccion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='direcciones')
    calle = models.CharField(max_length=255, blank=True, null=True)  # Cambiado a nullable
    colonia = models.CharField(max_length=100, blank=True, null=True)  # También puedes hacer esto para otros campos si es necesario
    numero = models.CharField(max_length=10, blank=True, null=True)
    codigo_postal = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return f"{self.calle}, {self.colonia}, {self.numero}, {self.codigo_postal}"