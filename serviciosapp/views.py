from django.shortcuts import render
from serviciosapp.models import Servicio

def servicios(request):

    servicios=Servicio.objects.all()
    return render(request, 'serviciosapp/servicios.html',{'servicios':servicios})

# Create your views here.
