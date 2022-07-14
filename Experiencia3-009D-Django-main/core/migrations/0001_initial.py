# Generated by Django 4.0.5 on 2022-06-14 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('nombre', models.CharField(max_length=25, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='apellido')),
                ('rut', models.CharField(max_length=9, primary_key=True, serialize=False, verbose_name='rut')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='codigo')),
                ('precio', models.IntegerField(verbose_name='precio')),
                ('marca', models.CharField(max_length=20, verbose_name='Marca')),
                ('nombre', models.CharField(max_length=25, verbose_name='nombre')),
            ],
        ),
    ]
