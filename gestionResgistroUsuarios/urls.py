from django.conf import settings
from django.urls import path
from gestionResgistroUsuarios.views import home, contacto, tienda
from django.conf.urls.static import static

urlpatterns = [
    path("home/", home, name="Home"),
    path("contacto/", contacto, name="Contacto"),
    path("tienda/", tienda, name="Tienda"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)