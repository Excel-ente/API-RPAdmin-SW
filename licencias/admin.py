from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Licencias)

class GrupoUsuariosInline(admin.StackedInline):
    model = GrupoUsuarios
    extra = 1
    fields = ('GRUPO','USUARIO','LICENCIA','FECHA_INICIO','FECHA_FINAL')

@admin.register(Grupo)
class adminRobots(admin.ModelAdmin):
    inlines = [
        GrupoUsuariosInline,
    ]
    list_display=('ADMINISTRADOR','LICENCIAS_ASIGNADAS','LICENCIAS_LIBRES')
    ordering=('ADMINISTRADOR',)
    search_fields= ('ADMINISTRADOR',)
    list_filter=('ADMINISTRADOR',)
    exclude=('USUARIOS','LICENCIAS_ASIGNADAS','LICENCIAS_LIBRES')


