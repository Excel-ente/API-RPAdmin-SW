# Generated by Django 4.2.1 on 2023-05-22 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licencias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='LICENCIAS_ASIGNADAS',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='grupo',
            name='LICENCIAS_LIBRES',
            field=models.IntegerField(default=1),
        ),
    ]
