from django.shortcuts import render
from blog.models import Post

def blog(request):

    posts=Post.objects.all()

    return render(request, "blog/blog.html",{'posts':posts} )

# Create your views here.
