# Generated by Django 4.2.1 on 2023-05-18 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0010_reprocesorobot_archivo_config_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reprocesorobot',
            options={'verbose_name': 'Reproceso', 'verbose_name_plural': 'Instructivo Reproceso'},
        ),
        migrations.AlterField(
            model_name='reprocesorobot',
            name='REPROCESAR',
            field=models.TextField(verbose_name='DETALLE'),
        ),
    ]
