from email.errors import MessageError
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from carro.carro import Carro
from pedidos.models import LinePedido, Pedido
from django.contrib import messages
from django.utils.html import strip_tags
from django.core.mail import send_mail


# Create your views here.
@login_required(login_url='/autenticacion/logear')
def procesar_pedidos(request):
    pedido=Pedido.objects.create(user=request.user)
    carro=Carro(request)

    lineas_pedido=list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LinePedido(

            producto_id=key,
            cantidad=value['cantidad'],
            user=request.user,
            pedido=pedido
        ))

    LinePedido.objects.bulk_create(lineas_pedido)

    #Llamada a funcion

    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        emailusuario=request.user.email
    )


    messages.success(request, 'El pedido ha sido agregado con éxito')

    return redirect('../tienda')

def enviar_mail(**kwargs):

    asunto='Gracias por el pedido'
    mensaje=render_to_string('emails/pedido.html',{
        'pedido': kwargs.get('pedido'),
        'lineas_pedido': kwargs.get('lineas_pedido'),
        'nombreusuario': kwargs.get('nombreusuario')
    })
    mensaje_texto=strip_tags(mensaje)
    from_email='rojasderinson@gmail.com'
    to=kwargs.get('emailusuario')

    send_mail(asunto,mensaje_texto,from_email,[to],html_message=mensaje)

