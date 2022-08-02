from mailbox import NoSuchMailboxError
from pyexpat import model
from tabnanny import verbose
from turtle import update
from django.db import models

# Create your models here.

class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name='Categoria del Productos'
        verbose_name_plural='Categoria de los productos'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    categorias=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='tienda', null=True, blank=True)
    disponibilidad=models.BooleanField(default=True)
    precio=models.FloatField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name='Producto'
        verbose_name_plural='Productos'





