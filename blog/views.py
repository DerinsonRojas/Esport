from django.shortcuts import render, redirect
from blog.models import Post, Categoria
from django.urls import reverse
from .models import CategoriaForm, Post, PostForm 
from django.contrib import messages


def vista_delete(request, post_id):
    
    posts=Post.objects.get(pk=post_id)
    try:
        post=Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        messages.error(request,'El post que quieres eliminar no existe')
    
    if post.autor!=request.user:
        messages.error("No eres el autor de este post")
        return redirect('blog')
    
    post.delete()
    messages.success(request, f'El post {post.titulo} ha sido eliminado!')
    #exito=reverse_lazy('blog')
    return reverse('blog/blog.html')



def add_post(request):
    poster=request.user

    form = PostForm(request.POST,request.FILES) # Bound form
    #form2 = CategoriaForm(request.POST)

    if form.is_valid():
        new_post=form.save(commit=False)
        new_post.autor = poster
        new_post.save()
        #messages.add_message(request,"El post se ha agregado con exito")
        return redirect('misEntradas')

    return render(request, 'blog/addPost.html', {'form': form})

def mod_post(request,post_id):
    post=Post.objects.get(pk=post_id)
    form=PostForm(request.POST or None, instance=post)
    if request.POST and form.is_valid():
        form.save()
        return redirect('misEntradas')
    #form2 = CategoriaForm(instance=entrada)

    return render(request, 'blog/modPost.html', {'form': form, 'post':post})


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
