# Generated by Django 4.0.5 on 2022-08-02 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_contenido_post_descripcion_post_contentenido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='contentenido',
            new_name='contenido',
        ),
    ]
