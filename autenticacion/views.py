from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm

class VRegistro(View):

    def get(self, request):
        form=UserCreationForm()
        return render(request, 'registro/registro.html', {'form':form})

    def post(self, requesst):
        pass




# Create your views here.
