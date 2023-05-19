# Generated by Django 4.2.1 on 2023-05-17 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aplicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOMBRE', models.CharField(max_length=255, unique=True)),
                ('VERSION', models.CharField(max_length=150)),
                ('APLICACION_INTERNA', models.BooleanField(default=False)),
                ('ULTIMA_MODIFICACION', models.DateField(auto_now_add=True)),
                ('APLICA_VENCIMIENTO', models.BooleanField(default=False)),
                ('FECHA_VENCIMIENTO', models.DateField(blank=True, null=True)),
                ('INFO', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Aplicaciones',
                'verbose_name_plural': 'Aplicaiones',
            },
        ),
        migrations.CreateModel(
            name='Gerencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GERENCIA', models.CharField(max_length=50)),
                ('PROCESOS_ACTIVOS', models.IntegerField(blank=True, null=True)),
                ('HORAS_BENEFICIO', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
            ],
            options={
                'verbose_name': 'Gerencia',
                'verbose_name_plural': 'Gerencias',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOMBRE_APELLIDO', models.CharField(max_length=120)),
                ('EMPRESA', models.CharField(blank=True, max_length=60, null=True)),
                ('CARGO', models.CharField(blank=True, max_length=50, null=True)),
                ('MAIL', models.EmailField(blank=True, max_length=254, null=True)),
                ('TELEFONO', models.CharField(blank=True, max_length=20, null=True)),
                ('COMENTARIOS', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOMBRE_APELLIDO', models.CharField(max_length=120)),
                ('MAIL', models.EmailField(blank=True, max_length=254, null=True)),
                ('TELEFONO', models.CharField(blank=True, max_length=20, null=True)),
                ('COMENTARIOS', models.TextField(blank=True, null=True)),
                ('GERENCIA', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='administracion.gerencia')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='servidores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HOSTNAME', models.CharField(max_length=20, unique=True)),
                ('IP', models.CharField(blank=True, max_length=20, null=True)),
                ('TIPO', models.CharField(choices=[('Desarrollo', 'Desarrollo'), ('Test', 'Test'), ('Pre-Produccion', 'Pre-Produccion'), ('Produccion', 'Produccion')], default=1, max_length=20)),
                ('SISTEMA_OPERATIVO', models.CharField(choices=[('Windows', 'Windows'), ('Linux', 'Linux'), ('Mac', 'Mac')], default=1, max_length=20)),
                ('PROCESADOR', models.CharField(blank=True, max_length=200, null=True)),
                ('MEMORIA_RAM', models.CharField(blank=True, max_length=20, null=True)),
                ('ARQUITECTURA', models.CharField(blank=True, max_length=20, null=True)),
                ('NOMBRE_COMPLETO', models.CharField(blank=True, max_length=50, null=True)),
                ('DOMINIO', models.CharField(blank=True, max_length=50, null=True)),
                ('COMENTARIOS', models.TextField(blank=True, null=True)),
                ('APLICACIONES_INSTALADAS', models.ManyToManyField(to='administracion.aplicacion')),
            ],
            options={
                'verbose_name': 'Servidor',
                'verbose_name_plural': 'Servidores',
            },
        ),
        migrations.CreateModel(
            name='robots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ACTIVO', models.BooleanField(default=False)),
                ('NOMBRE', models.CharField(max_length=120, unique=True)),
                ('FECHA_PUESTA_PRD', models.DateField(blank=True, null=True)),
                ('ATENDIDO', models.CharField(choices=[('Atendido', 'Atendido'), ('Desatendido', 'Desatendido')], default='ATENDIDO', max_length=11)),
                ('ULTIMO_PAQUETE', models.CharField(blank=True, max_length=20, null=True)),
                ('ULTIMA_ACTUALIZACION', models.DateField(blank=True, null=True)),
                ('ARCHIVO_CONFIG', models.CharField(max_length=255)),
                ('RUTAS_INPUT', models.CharField(blank=True, max_length=255, null=True)),
                ('RUTAS_OUTPUT', models.CharField(blank=True, max_length=255, null=True)),
                ('DESCRIPCION_BREVE', models.TextField(blank=True, null=True)),
                ('COMENTARIOS', models.TextField(blank=True, null=True)),
                ('EJECUCIONES', models.IntegerField(blank=True, null=True)),
                ('ERRORES', models.IntegerField(blank=True, null=True)),
                ('FATAL', models.IntegerField(blank=True, null=True)),
                ('GERENCIA', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='administracion.gerencia')),
                ('PROVEEDOR', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='administracion.proveedor')),
                ('SERVIDOR', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='administracion.servidores')),
                ('USUARIO', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='administracion.usuario')),
            ],
            options={
                'verbose_name': 'Robot',
                'verbose_name_plural': 'Robots',
            },
        ),
        migrations.CreateModel(
            name='ejecucionesProcesos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TIPO_EJECUCION', models.CharField(choices=[('Diario', 'Diario'), ('Quincenal', 'Quincenal'), ('Mensual', 'Mensual'), ('Bimestral', 'Bimestral'), ('Trimestral', 'Trimestral'), ('Semestral', 'Semestral'), ('Anual', 'Anual')], default='Diario', max_length=20)),
                ('DOM', models.BooleanField(default=False)),
                ('LUN', models.BooleanField(default=False)),
                ('MAR', models.BooleanField(default=False)),
                ('MIE', models.BooleanField(default=False)),
                ('JUE', models.BooleanField(default=False)),
                ('VIE', models.BooleanField(default=False)),
                ('SAB', models.BooleanField(default=False)),
                ('CANTIDAD_EJECUCIONES_MENSUALES', models.IntegerField(blank=True, default=0, null=True)),
                ('ESPACIO_AGENDA_MIN', models.IntegerField(blank=True, default=15, null=True, verbose_name='MINUTOS RESERVADOS EN AGENDA')),
                ('EJECUCIONES_ACUMULADO', models.BigIntegerField(blank=True, null=True, verbose_name='ACUM. EJECUCIONES (30 dias)')),
                ('DURACION_TAREA_MINUTOS_MANUAL', models.IntegerField(null=True, verbose_name='DURACION DE LA TAREA (manualmente) Min.')),
                ('DURACION_MENSUAL', models.IntegerField(null=True, verbose_name='HS LABORABLES MENSUALES')),
                ('TIPO_ESFUERZO', models.CharField(choices=[('Bajo', 'Bajo'), ('Medio', 'Medio'), ('Alto', 'Alto')], default='Medio', max_length=10)),
                ('FTE', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='FTE')),
                ('CONSUMO_TOTAL', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, verbose_name='TOTAL HORAS AGENDA (mensual)')),
                ('COMENTARIOS', models.TextField(blank=True, null=True)),
                ('FECHA_INICIO', models.DateField(blank=True, null=True)),
                ('HORA_INICIO_EJECUCION', models.TimeField(blank=True, null=True)),
                ('HORA_FIN_CALCULADA', models.TimeField(blank=True, null=True)),
                ('LISTA', models.TextField(blank=True, null=True)),
                ('ROBOT', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='administracion.robots')),
                ('SERVIDOR', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='administracion.servidores')),
            ],
            options={
                'verbose_name': 'Ejecucion',
                'verbose_name_plural': 'Ejecuciones',
            },
        ),
        migrations.CreateModel(
            name='aplicacionesServidores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VERSION', models.CharField(blank=True, max_length=255, null=True)),
                ('APLICACION', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.aplicacion')),
                ('SERVIDOR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.servidores')),
            ],
            options={
                'verbose_name': 'Aplicacion',
                'verbose_name_plural': 'Aplicaciones instaladas',
            },
        ),
    ]
