from django.shortcuts import render, redirect
from django.core.mail import EmailMessage

from .forms import FormularioContacto

def contacto(request):

    formulario_contacto=FormularioContacto()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje de app Django",
            "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(nombre, email, contenido), 
            '',
            ["rojasderinson@gmail.com"], 
            reply_to=[email])

            try:
                email.send()

                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")


    

    return render(request, "contacto/contacto.html", {'miFormulario':formulario_contacto})
# Create your views here.
