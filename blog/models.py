from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.core.exceptions import NON_FIELD_ERRORS
import os


# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=50,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombre
 
class Post(models.Model):
    titulo=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    contenido = models.TextField(null=True, blank=True)
    imagen=models.ImageField(upload_to='blog', null=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    categorias=models.ManyToManyField(Categoria)
    
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def delete(self, *args,**kwargs):
        if os.path.isfile(self.imagen.path):
                os.remove(self.imagen.path)
        super(Post,self).delete(*args,**kwargs)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'

    def __str__(self):
        return self.titulo

class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=['titulo','descripcion','contenido','imagen','categorias']
        

class CategoriaForm(ModelForm):
    class Meta:
        model=Categoria
        fields=['nombre']

class ArticleForm(ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }