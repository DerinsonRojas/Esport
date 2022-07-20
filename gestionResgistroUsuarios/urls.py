from django.urls import include, path
from gestionResgistroUsuarios.views import home, contacto, servicios, blog, tienda

urlpatterns = [
    path("home/", home, name="Home"),
    path("contacto/", contacto, name="Contacto"),
    path("servicios/", servicios, name="Servicios"),
    path("blog/", blog, name="Blog"),
    path("tienda/", tienda, name="Tienda"),
]

