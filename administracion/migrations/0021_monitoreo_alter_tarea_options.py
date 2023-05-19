# Generated by Django 4.2.1 on 2023-05-18 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0020_delete_monitoreo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monitoreo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo', models.TextField(blank=True, null=True)),
                ('Fecha', models.DateField(blank=True, null=True)),
                ('HoraEjecucion', models.TextField(blank=True, null=True)),
                ('Proceso', models.TextField(blank=True, null=True)),
                ('Gerencia', models.TextField(blank=True, null=True)),
                ('Mensaje', models.TextField(blank=True, null=True)),
                ('Duracion', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Duracion Minutos')),
                ('Server', models.TextField(blank=True, null=True)),
                ('Paquete', models.TextField(blank=True, null=True)),
                ('Comentarios', models.CharField(blank=True, max_length=120, null=True)),
                ('clave', models.TextField(blank=True, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Monitoreo',
                'verbose_name_plural': 'Monitoreos',
            },
        ),
        migrations.AlterModelOptions(
            name='tarea',
            options={'verbose_name': 'Tarea', 'verbose_name_plural': 'Tareas'},
        ),
    ]
