from django.contrib import admin

from .models import Pedido, LinePedido

# Register your models here.

admin.site.register([Pedido, LinePedido])