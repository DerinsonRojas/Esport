from django.shortcuts import render, HttpResponse



def home(request):

    return render(request, "gestionResgistroUsuarios/home.html")

def tienda(request):

    return render(request, "gestionResgistroUsuarios/tienda.html")



# Create your views here.
