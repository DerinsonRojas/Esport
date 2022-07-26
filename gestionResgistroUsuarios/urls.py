from django.conf import settings
from django.urls import include, path
from gestionResgistroUsuarios.views import home, contacto, blog, tienda
from django.conf.urls.static import static

urlpatterns = [
    path("home/", home, name="Home"),
    path("contacto/", contacto, name="Contacto"),
    path("blog/", blog, name="Blog"),
    path("tienda/", tienda, name="Tienda"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)