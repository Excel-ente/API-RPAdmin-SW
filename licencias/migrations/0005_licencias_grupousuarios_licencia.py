# Generated by Django 4.2.1 on 2023-05-22 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('licencias', '0004_remove_grupo_nombre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Licencias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOMBRE', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='grupousuarios',
            name='LICENCIA',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='licencias.licencias'),
            preserve_default=False,
        ),
    ]