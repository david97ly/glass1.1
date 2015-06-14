from django.db import models

# Create your models here.
class Order(models.Model):
    orden = models.CharField(max_length = 10)

    def __unicode__(self):
        return "%s " % (self.orden)
	

class Fotos(models.Model):
	nombre = models.CharField(max_length=500)
	ruta = models.ImageField(upload_to='photos')
	valida = models.BooleanField(default=False)


class Slide(models.Model):
	mensaje = models.CharField(max_length=500)
	submensaje = models.CharField(max_length=500)
	valida = models.BooleanField(default=False)
	orden = models.ForeignKey(Order)
	foto = models.ImageField(upload_to='photos')

			
class Mensajeb(models.Model):
	mensaje = models.CharField(max_length=500)
	submensaje = models.CharField(max_length=500)
	valida = models.BooleanField(default=False)
	
	
class Info(models.Model):
	titulo = models.CharField(max_length=500)
	subtitulo = models.CharField(max_length=500)
	informacion = models.TextField(max_length=100)
	valida = models.BooleanField(default=False)
	orden = models.ForeignKey(Order)
	foto = models.ImageField(upload_to='photos')

	
class Contactos(models.Model):
	telefono1 = models.CharField(max_length=500)
	telefono2 = models.CharField(max_length=500)
	correo = models.CharField(max_length=500)
	fax = models.CharField(max_length=500)
	address = models.CharField(max_length=500)

	
class Servicios(models.Model):
	titulo = models.CharField(max_length=500)
	informacion = models.TextField(max_length=100)
	valida = models.BooleanField(default=False)
	foto = models.ImageField(upload_to='photos')

	