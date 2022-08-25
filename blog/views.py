from django.shortcuts import render, redirect
from blog.models import Post, Categoria
from .models import CategoriaForm, Post, PostForm 
from django.views.generic import DeleteView
from django.urls import reverse_lazy

class DeletePostView(DeleteView):
    model=Post
    template_name='blog/delete_post.html'
    success_url=reverse_lazy('misEntradas')

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

    posts=Post.objects.all().order_by('-created')

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

def nuevaCat(request):

    form = CategoriaForm(request.POST,request.FILES)

    if request.method=='POST':

        if form.is_valid():

            form.save()
    
        return redirect('addPost')
        
    
    return render(request, 'blog/nuevacat.html', {'categoria':categoria, 'form':form})
# Create your views here.
