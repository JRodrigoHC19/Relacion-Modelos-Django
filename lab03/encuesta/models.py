from django.db import models

# Create your models here.
class Pregunta(models.Model):
    pregunta_texto = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    opcion_texto = models.CharField(max_length=200)
    votos = models.BigIntegerField(default=0)



class Proveedor(models.Model):
    prov_cod = models.IntegerField(primary_key=True)
    prov_name = models.CharField(max_length=100)
    prov_direc = models.CharField(max_length=100)
    prov_telf = models.IntegerField()
    prov_url = models.CharField(max_length=500)

class Cliente(models.Model):
    cli_cod = models.IntegerField(primary_key=True)
    cli_name = models.CharField(max_length=100)
    cli_direc = models.CharField(max_length=100)
    cli_telf_1 = models.IntegerField()
    cli_telf_2 = models.IntegerField()

class Clasificacion(models.Model):
    cla_cod = models.IntegerField(primary_key=True)
    cla_name = models.CharField(max_length=100)
    descrip = models.CharField(max_length=500)


class Producto(models.Model):
    prod_cod = models.BigIntegerField(primary_key=True)
    prod_name = models.CharField(max_length=50)
    precio = models.FloatField()
    stock = models.IntegerField()
    proveedor_name = models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    clasificacion_cod = models.ForeignKey(Clasificacion, on_delete=models.CASCADE)

class Venta(models.Model):
    nro_fac = models.BigIntegerField(primary_key=True)
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descuento = models.FloatField()
    producto_cod = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    monto = models.FloatField()
