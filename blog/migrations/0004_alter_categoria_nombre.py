# Generated by Django 4.0.5 on 2022-08-22 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_contentenido_post_contenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
