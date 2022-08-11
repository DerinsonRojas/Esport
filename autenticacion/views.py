from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import Permission, User, Group
from blog.models import Post, Categoria
from django.contrib.contenttypes.models import ContentType
from .forms import CustomUserCreationForm  

class VRegistro(View):

    def get(self, request):
        form=CustomUserCreationForm() 
        return render(request, 'registro/registro.html', {'form':form})

    def post(self, request):
        form=CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            usuario=form.save()

            #Asignacion de permisos a usuarios creados
            content_type = ContentType.objects.get_for_model(Post)
            post_permission = Permission.objects.filter(content_type=content_type)

            for perm in post_permission:
                usuario.user_permissions.add(perm)

            content_type = ContentType.objects.get_for_model(Categoria)
            categoria_permission = Permission.objects.filter(content_type=content_type)
            for perm in categoria_permission:
                if perm.codename=='delete_categoria':
                    continue
                else:
                    usuario.user_permissions.add(perm)

            #---------------------Fin de la asignación de permisos

            messages.success(request, 'Cuenta creada correctamente')
            login(request, usuario)
            #return render(request, 'login/login.html')
            return redirect('Home')

        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            return render(request, 'registro/registro.html', {'form':form})
'''

def VRegistro(request):  
    if request.POST == 'POST':  
        form = CustomUserCreationForm()  
        if form.is_valid():  
            form.save()
            print('Funnciona')
        return redirect('Home')  
    else:
        print('No Funnciona')
        form = CustomUserCreationForm()
        contexto = { 'form':form}    
        return render(request, 'registro/registro.html',contexto)  
      
'''     


def cerrar_sesion(request):
    logout(request)

    return redirect('Home')


def logear(request):
    if request.method=='POST':
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get('username')
            contra=form.cleaned_data.get('password')
            usuario=authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
            else:
                messages.error(request, 'Usuario no válido')
        else:
            messages.error(request,'Información incorrecta')

    form=AuthenticationForm()
    return render(request, 'login/login.html', {'form':form})



# Create your views here.
