from django.urls import path
from . import views
from .views import DeletePostView

urlpatterns = [
    path("", views.blog, name="Blog"),
    path("categoria/<int:categoria_id>/", views.categoria, name="categoria"),
    path("misEntradas/", views.misEntradas, name="misEntradas"),
    path("addPost/",views.add_post,name='addPost'),
    path("entrada/<int:post_id>/", views.entrada, name="valordelnameentrada"),
    path("modPost/<int:post_id>/",views.mod_post,name='modPost'),
    path("delete_post/<int:pk>/", DeletePostView.as_view(),name='delete_post'),
]
