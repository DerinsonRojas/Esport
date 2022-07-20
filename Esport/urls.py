"""Esport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestionResgistroUsuarios.views import home, contacto, servicios, tienda, blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", home, name="Home"),
    path("contacto/", contacto, name="Contacto"),
    path("servicios/", servicios, name="Servicios"),
    path("blog/", blog, name="Blog"),
    path("tienda/", tienda, name="Tienda"),
]
