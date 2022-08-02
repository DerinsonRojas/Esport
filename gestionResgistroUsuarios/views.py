from django.shortcuts import render, HttpResponse



def home(request):

    return render(request, "gestionResgistroUsuarios/home.html")




# Create your views here.
