from django.db import models
from administracion.models import Usuario
# Create your models here.



class Licencias(models.Model):
    NOMBRE=models.CharField(max_length=255,blank=False,null=False)

    def __str__(self):
        return self.NOMBRE

class Grupo(models.Model):
    ADMINISTRADOR=models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='grupos_administrador', blank=False, null=False)
    USUARIOS=models.ManyToManyField(Usuario)
    LICENCIAS_ASIGNADAS=models.IntegerField(default=1,blank=False, null=False)
    LICENCIAS_LIBRES=models.IntegerField(default=1,blank=False, null=False)

class GrupoUsuarios(models.Model):
    GRUPO=models.ForeignKey(Grupo,on_delete=models.CASCADE)
    USUARIO=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    LICENCIA=models.ForeignKey(Licencias,on_delete=models.CASCADE,blank=True, null=True)
    FECHA_INICIO=models.DateField(blank=True, null=True)
    FECHA_FINAL=models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Usuarios'
        verbose_name_plural ='Usuarios Asignados' 
        unique_together = ('GRUPO', 'USUARIO')