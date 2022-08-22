from django.shortcuts import render, redirect
from blog.models import Post, Categoria
from django.views.generic import ListView

from .models import Post 

def add_post(request):
    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form = Post(request.POST) # Bound form
        if form.is_valid():
            new_post = form.save() # Guardar los datos en la base de datos

            return redirect(("blog/misEntradas.html"))
    else:
        form = Post() # Unbound form

    return render(request, 'blog/persona_form.html', {'form': form})

class BlogList(ListView):
    model=Post



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
    
    posts=Post.objects.all()

    categoria=Categoria.objects.all()    

    return render(request, "blog/misEntradas.html",{'posts':posts,'categoria':categoria})
# Create your views here.
