from django.shortcuts import render
from blog.models import Post, Categoria


def blog(request):

    posts=Post.objects.all()

    return render(request, "blog/blog.html",{'posts':posts} )

def categoria(request, categoria_id):

    categoria=Categoria.objects.get(id=categoria_id)

    posts=Post.objects.filter(categorias=categoria)#Para que los post que aparezcan en la vista aparezcan filtrados por categoria

    return render(request, "blog/categoria.html",{'categoria':categoria,'posts':posts})

def entrada(request, post_id):

    posts=Post.objects.get(id=post_id)

    entrada=Post.objects.filter(id=post_id)

    return render(request, "blog/entrada.html",{entrada:'entrada','posts':posts})

def misEntradas(request):
    

    return render(request, "blog/misEntradas.html" )

# Create your views here.
