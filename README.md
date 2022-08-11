# Esport
Backend para página de Esports.
Hasta ahora este proyecto se realiza de manera LOCAL (mismas dependencias para todos los proyectos)
por lo que deberá instalar las mismas versiones de python y django en su ordenador en función de observar los 
mismos resultados, además evitar problemas de compatibilidad.
Hata ahora se ha desarrollado el proyecto con:
- Python 3.10.4
- Django 4.0.5
- La base de datos usada es SQL3 y viene integrada por defecto en Django por lo que no deberá instalar nada respecto a BBDD

-Para el buen funcionamiento de la carga de imagenes en nuevas APIS instalar en la terminal, pip install Pillow
-Instala pip install django-crispy-forms para el correcto funcionamiento de los formularios 
-Instalar pip install python-decouple para las variables de entorno

Para inicializar el servidor en la terminal y desde el directorio principal 
del proyecto se utiliza la instrucción python manage.py runserver, el proyecto sera accesible desde 
el puerto 8000. Ej: http://127.0.0.1:8000/home/  le dará acceso a la vista principal desde la cual
podrá interactuar con el sitio en general


