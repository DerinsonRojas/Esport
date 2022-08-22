from django.shortcuts import render, redirect
from blog.models import Post, Categoria
from django.views.generic import ListView

from .models import CategoriaForm, Post, PostForm 

def add_post(request):
    form = PostForm(request.POST,request.FILES) # Bound form
    form2 = CategoriaForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('misEntradas')

    return render(request, 'blog/addPost.html', {'form': form, 'form2':form2})

def mod_post(request,post_id):
    entrada=Post.objects.get(pk=post_id)
    form=PostForm(instance=entrada)
    #form2 = CategoriaForm(instance=entrada)
    
     
     

    return render(request, 'blog/modPost.html', {'form': form})

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

    return render(request, "blog/entrada.html",{'posts':posts})

def misEntradas(request):
    
    posts=Post.objects.all()

    categoria=Categoria.objects.all()    

    return render(request, "blog/misEntradas.html",{'posts':posts,'categoria':categoria})
# Create your views here.
