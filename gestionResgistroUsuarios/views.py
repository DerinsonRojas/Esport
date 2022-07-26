from django.shortcuts import render, HttpResponse



def home(request):

    return render(request, "gestionResgistroUsuarios/home.html")

def tienda(request):

    return render(request, "gestionResgistroUsuarios/tienda.html")


def contacto(request):

    return render(request, "gestionResgistroUsuarios/contacto.html")

# Create your views here.
