# Generated by Django 4.2.1 on 2023-05-18 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0013_alter_robots_proveedor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reprocesorobot',
            name='ARCHIVO_CONFIG',
        ),
        migrations.RemoveField(
            model_name='reprocesorobot',
            name='RUTAS_INPUT',
        ),
        migrations.RemoveField(
            model_name='reprocesorobot',
            name='RUTAS_OUTPUT',
        ),
    ]
