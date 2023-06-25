from django.db import models


# Create your models here.


class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)


class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    id_genero = models.ForeignKey('Genero', on_delete=models.CASCADE, db_column='idGenero')
    telefono = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.nombre) + " " + str(self.apellido_paterno)

    class Meta:
        ordering = ['rut']


class Producto(models.Model):
    prod_id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    precio = models.IntegerField()

    class Meta:
        ordering = ['prod_id']

# class Vehiculo(models.Model):
# id = models.IntegerField(primary_key=True, max_length=6)
