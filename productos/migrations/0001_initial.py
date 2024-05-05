# Generated by Django 5.0.4 on 2024-05-03 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productoNombre', models.CharField(max_length=150)),
                ('productoImg', models.ImageField(upload_to='productos/')),
                ('productoDescripcion', models.TextField()),
                ('productoDescripcionSimple', models.TextField()),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
        ),
    ]