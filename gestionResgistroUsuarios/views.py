from django.shortcuts import render, HttpResponse

from carro.carro import Carro




def home(request):

    carro=Carro(request)

    return render(request, "gestionResgistroUsuarios/home.html")




# Create your views here.
