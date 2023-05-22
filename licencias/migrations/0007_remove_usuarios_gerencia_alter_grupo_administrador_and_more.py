# Generated by Django 4.2.1 on 2023-05-22 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0002_alter_aplicacion_id_alter_aplicacionesrobot_id_and_more'),
        ('licencias', '0006_alter_grupousuarios_licencia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='GERENCIA',
        ),
        migrations.AlterField(
            model_name='grupo',
            name='ADMINISTRADOR',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='grupos_administrador', to='administracion.usuario'),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='USUARIOS',
            field=models.ManyToManyField(to='administracion.usuario'),
        ),
        migrations.AlterField(
            model_name='grupousuarios',
            name='USUARIO',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.usuario'),
        ),
        migrations.DeleteModel(
            name='Gerencia',
        ),
        migrations.DeleteModel(
            name='Usuarios',
        ),
    ]