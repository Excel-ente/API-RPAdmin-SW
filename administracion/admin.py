
# --------------------------------------------------------------
# Administradores de vistas RPAdmin - Administracion
#
# Desarrollador: Kevin Turkienich - 2023
# --------------------------------------------------------------

#librerias de ORM de Django
from os import path
from django import forms
from django.contrib import admin

#libreria para importar/exportad datos
from import_export.admin import ImportExportModelAdmin

#Importacion de modelos
from administracion.models import reprocesoRobot,aplicacionesServidores,Aplicacion,servidores,Gerencia,Usuario,Proveedor,ejecucionesProcesos,robots,aplicacionesRobot,incidencias,Tarea

#Libreria para filtros
from django.utils.translation import gettext_lazy as _


#Header de sitio
admin.site.site_header = "RPAdmin"
admin.site.site_title = "Sistema de gestion de procesos"


# ----------------------------------------------------------------------------------------------------
# Administradores de vistas:
#
# ----------------------------------------------------------------------------------------------------

'''
class ServidorFilter(admin.SimpleListFilter):
    title = _('Servidor')
    parameter_name = 'servidor'

    def lookups(self, request, model_admin):
        servidores = model_admin.get_queryset(request).values_list('SERVIDOR', flat=True).distinct()
        return [(servidor, servidor) for servidor in servidores]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(SERVIDOR=self.value())
        else:
            return queryset
'''

class ActivoFilter(admin.SimpleListFilter):
    title = _('Activo')
    parameter_name = 'activo'

    def lookups(self, request, model_admin):
        return (
            ('1', _('Sí')),
            ('0', _('No')),
        )

    def queryset(self, request, queryset):
        if self.value() == '1':
            return queryset.filter(ACTIVO=True)
        elif self.value() == '0':
            return queryset.filter(ACTIVO=False)
        else:
            return queryset

class aplicacionesRobotInline(admin.TabularInline):
    model = aplicacionesRobot
    extra = 1

class reprocesoRobotInline(admin.StackedInline):
    model = reprocesoRobot
    extra = 1


@admin.register(robots)
class adminRobots(ImportExportModelAdmin):
    inlines = [
        aplicacionesRobotInline,
        reprocesoRobotInline,
    ]
    list_display=('NOMBRE','ACTIVO','PRODUCCION','USUARIO','GERENCIA','PROVEEDOR',)
    ordering=('NOMBRE',)
    search_fields= ('NOMBRE','NOMBRE','USUARIO','GERENCIA','PROVEEDOR',)
    list_per_page = 50
    list_filter=('NOMBRE','NOMBRE','USUARIO','GERENCIA','PROVEEDOR')
    list_display_links=('NOMBRE',)
    exclude =('COMENTARIOS','ULTIMA_ACTUALIZACION','EJECUCIONES','ERRORES','FATAL','APLICACIONES_USADAS','REPROCESAR',)

class aplicacionesServidoresInline(admin.TabularInline):
    model = aplicacionesServidores
    extra = 1

    

@admin.register(servidores)
class adminServidores(ImportExportModelAdmin):
    inlines = [
        aplicacionesServidoresInline,
    ]
    list_display=('HOSTNAME','TIPO','SISTEMA_OPERATIVO','PROCESADOR','MEMORIA_RAM','ARQUITECTURA','DOMINIO','COMENTARIOS',)
    ordering=('TIPO',)
    search_fields= ('HOSTNAME',)
    list_per_page = 20
    list_display_links=('HOSTNAME',)
    exclude=('APLICACIONES_INSTALADAS',)


@admin.register(Gerencia)
class adminRobots(ImportExportModelAdmin):
    list_display=('GERENCIA','PROCESOS_ACTIVOS',)
    exclude=('PROCESOS_ACTIVOS','HORAS_BENEFICIO',)

@admin.register(Usuario)
class adminRobots(ImportExportModelAdmin):
    list_display=('NOMBRE_APELLIDO','GERENCIA','MAIL','TELEFONO','COMENTARIOS',)
    list_filter=('NOMBRE_APELLIDO','GERENCIA',)


@admin.register(Proveedor)
class adminRobots(ImportExportModelAdmin):
    list_display=('NOMBRE_APELLIDO','EMPRESA','CARGO','MAIL','TELEFONO','COMENTARIOS',)

@admin.register(ejecucionesProcesos)
class adminEjecuciones(ImportExportModelAdmin):

    list_display=('ROBOT','HORA_INICIO_EJECUCION','HORA_FIN_CALCULADA','SERVIDOR','TIPO_EJECUCION','ESPACIO_AGENDA_MIN','CONSUMO_TOTAL','DURACION_MENSUAL','CANTIDAD_EJECUCIONES_MENSUALES','FTE','COMENTARIOS',)
    ordering=('CONSUMO_TOTAL',)
    list_filter=('SERVIDOR',)
    exclude=('FTE','CONSUMO_TOTAL','EJECUCIONES_ACUMULADO','SERVIDOR','CANTIDAD_EJECUCIONES_MENSUALES','LISTA','HORA_FIN_CALCULADA',)
    list_per_page = 100

@admin.register(Aplicacion)
class adminAplicacion(ImportExportModelAdmin):
    list_display=('NOMBRE','VERSION','APLICACION_INTERNA','FECHA_VENCIMIENTO',)
    ordering=('NOMBRE',)

@admin.register(incidencias)
class adminAplicacion(ImportExportModelAdmin):
    list_display = ('N_INCIDENTE', 'ROBOT', 'ESTADO', 'ASIGNADO_A', 'ULTIMA_ACTUALIZACION',)
    ordering = ('N_INCIDENTE',)
    list_filter = ('ESTADO',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Si el filtro "Finalizado" está seleccionado, mostrar todos los incidentes
        if 'ESTADO__exact' in request.GET and request.GET['ESTADO__exact'] == 'Finalizado':
            return qs

        # Filtrar por defecto los incidentes con estado diferente a "Finalizado"
        qs = qs.exclude(ESTADO="Finalizado")
        return qs

@admin.register(Tarea)
class adminTarea(admin.ModelAdmin):
    list_display=('NOMBRE','ESTADO','FECHA_INICIO','FECHA_FIN','TIEMPO_INVERTIDO','GERENCIA_A_IMPUTAR',)
    ordering=('FECHA_INICIO',)

    change_list_template = 'admin/tarea/change_list.html'

    class Media:
        css = {
            'all': ('css/admin.css',),
        }

