# Generated by Django 5.0.4 on 2024-05-05 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_alter_producto_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='productoDescripcion',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='producto',
            name='productoDescripcionSimple',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='producto',
            name='productoNombre',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
