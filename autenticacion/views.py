from django.shortcuts import render
from serviciosapp.models import Servicio

def autenticacion(request):

    return render(request, 'autenticacion/autenticacion.html')

# Create your views here.
