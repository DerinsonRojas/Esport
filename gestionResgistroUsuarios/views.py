from django.shortcuts import render, HttpResponse

def home(request):

    return render(request, "gestionResgistroUsuarios/home.html")

def servicios(request):

    return render(request, "gestionResgistroUsuarios/servicios.html")

def tienda(request):

    return render(request, "gestionResgistroUsuarios/tienda.html")

def blog(request):

    return render(request, "gestionResgistroUsuarios/blog.html")

def contacto(request):

    return render(request, "gestionResgistroUsuarios/contacto.html")

# Create your views here.
