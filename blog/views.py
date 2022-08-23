from django.shortcuts import render, redirect, reverse, get_object_or_404
from blog.models import Post, Categoria
from django.views.generic import ListView
from django.http import HttpResponseForbidden
from .models import CategoriaForm, Post, PostForm 
from django.contrib.auth.decorators import login_required


@login_required
def edit(request, id=None, template_name='article_edit_template.html'):
    if id:
        article = get_object_or_404(Post, pk=id)
        if article.autor != request.user:
            return HttpResponseForbidden()
    else:
        article = Post(autor_id=request.user)

    form3 = PostForm(request.POST or None, instance=article)
    if request.POST and form3.is_valid():
        form3.save()

        # Save was successful, so redirect to another page
        
        return redirect('misEntradas')

    return render(request, 'blog/article_edit_template.html', {
        'form3': form3
    })

def add_post(request):
    poster=request.user

    form = PostForm(request.POST,request.FILES) # Bound form
    form2 = CategoriaForm(request.POST)

    if form.is_valid():
        new_post=form.save(commit=False)
        new_post.autor = poster
        new_post.save()
        return redirect('misEntradas')

    return render(request, 'blog/addPost.html', {'form': form, 'form2':form2})

def mod_post(request,post_id):
    entrada=Post.objects.get(pk=post_id)
    form=PostForm(request.POST or None, instance=entrada)
    if request.POST and form.is_valid():
        form.save()
        return redirect('misEntradas')
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
