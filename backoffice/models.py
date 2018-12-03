from django.db import models

# Create your models here.


class Pais(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Departamento(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Provincia(models.Model):
    nombre = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Distrito(models.Model):
    nombre = models.CharField(max_length=50)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Estacionamiento(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    costo = models.IntegerField(default=0)
    latitud = models.DecimalField(max_digits=9, decimal_places=7, default=0)
    longitud = models.DecimalField(max_digits=9, decimal_places=7, default=0)

    def __str__(self):
        return self.nombre
