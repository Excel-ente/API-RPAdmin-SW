# Generated by Django 4.2.1 on 2023-05-18 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0023_alter_robots_desarrollo_alter_robots_produccion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidencias',
            name='ASIGNADO_A',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administracion.usuario'),
        ),
        migrations.AlterField(
            model_name='incidencias',
            name='ROBOT',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.robots'),
        ),
    ]
