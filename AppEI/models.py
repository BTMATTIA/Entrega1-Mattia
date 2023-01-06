from django.db import models

# Create your models here.


class Terror(models.Model):
    titulo= models.CharField(max_length=50) #lo defino como un caracter de base de datos
    valoracion=models.IntegerField(max_length=2) #lo defino como un entero de base de datos

    def __str__(self):
        return f"{self.titulo} - {str(self.valoracion)}"

class Comedia(models.Model):
    titulo= models.CharField(max_length=50) #lo defino como un caracter de base de datos
    valoracion=models.CharField(max_length=2)  

    def __str__(self):
        return f"{self.titulo} - {str(self.valoracion)}"    

class Accion(models.Model):
    titulo= models.CharField(max_length=50) #lo defino como un caracter de base de datos
    valoracion= models.CharField(max_length=2)

    def __str__(self):
        return f"{self.titulo} - {str(self.valoracion)}"
