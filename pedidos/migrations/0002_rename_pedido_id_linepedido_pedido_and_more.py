
# Generated by Django 4.0.5 on 2022-08-08 21:43

# Generated by Django 4.0.5 on 2022-08-09 16:30


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='linepedido',
            old_name='pedido_id',
            new_name='pedido',
        ),
        migrations.RenameField(
            model_name='linepedido',
            old_name='producto_id',
            new_name='producto',
        ),
    ]
