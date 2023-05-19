# ----------------------------------------------------------
# Modelos de bases de datos RPAdmin
#
# Desarrollador: Kevin Turkienich - 2023
# ----------------------------------------------------------

#librerias de ORM de Django
from django.db import models

#librerias para trabajar con formatos de tiempo
from datetime import datetime, timedelta

from django.forms import ValidationError

#Importacion de las listas
from .listas import *

# --------------------------------------
# Modelos de bases de datos:
#
# --------------------------------------

#-----------------------------------------------------------------------------------------------
#>>>> MODELO GERENCIAS
class Gerencia(models.Model):
    GERENCIA=models.CharField(max_length=50,null=False,blank=False)
    PROCESOS_ACTIVOS=models.IntegerField(blank=True,null=True)
    HORAS_BENEFICIO=models.DecimalField(max_digits=8,decimal_places=2,blank=True,null=True)
    
    class Meta:
        verbose_name = 'Gerencia'
        verbose_name_plural ='ABM Gerencias'

    def __str__(self):
        return self.GERENCIA

#-----------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------
#>>>> MODELO USUARIOS
class Usuario(models.Model):
    NOMBRE_APELLIDO=models.CharField(max_length=120,null=False,blank=False) 
    GERENCIA=models.ForeignKey(Gerencia,on_delete=models.PROTECT,null=True,blank=True)
    MAIL=models.EmailField(blank=True,null=True)
    TELEFONO= models.CharField(max_length=20,null=True,blank=True)
    COMENTARIOS=models.TextField(null=True,blank=True)
 
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural ='ABM Usuarios'

    def __str__(self):
        return self.NOMBRE_APELLIDO

#-----------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------
#>>>> MODELO PROVEEDORES
class Proveedor(models.Model):
    NOMBRE_APELLIDO=models.CharField(max_length=120,null=False,blank=False) 
    EMPRESA=models.CharField(max_length=60,null=True,blank=True)
    CARGO=models.CharField(max_length=50,null=True,blank=True)
    MAIL=models.EmailField(blank=True,null=True)
    TELEFONO= models.CharField(max_length=20,null=True,blank=True)
    COMENTARIOS=models.TextField(null=True,blank=True)

    class Meta:
        verbose_name = 'Desarrollador'
        verbose_name_plural ='ABM Desarrolladores'

    def __str__(self): 
        return self.NOMBRE_APELLIDO 

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
#>>>> MODELO APLICACIONES
class Aplicacion(models.Model):
    NOMBRE=models.CharField(max_length=255,null=False,blank=False,unique=True)
    VERSION=models.CharField(max_length=150,null=False,blank=False)
    APLICACION_INTERNA=models.BooleanField(default=False)
    ULTIMA_MODIFICACION=models.DateField(auto_now_add=True,blank=False,null=False)
    APLICA_VENCIMIENTO=models.BooleanField(default=False)
    FECHA_VENCIMIENTO=models.DateField(blank=True,null=True)
    INFO=models.TextField(null=True,blank=True)

    class Meta:
        verbose_name = 'Aplicacion'
        verbose_name_plural ='ABM Aplicaciones'

    def __str__(self):
        if self.VERSION:
            if self.APLICA_VENCIMIENTO:
                fecha_vencimiento = self.FECHA_VENCIMIENTO.strftime("%d/%m/%Y")
                mensaje = f'{self.NOMBRE} | Version: {self.VERSION} | Venc: 📆{fecha_vencimiento}'
            else:
                mensaje = f'{self.NOMBRE} Version: {self.VERSION}'
        else:
            mensaje = self.NOMBRE
        return mensaje

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
#>>>> MODELO SERVIDORES 
class servidores(models.Model):
    HOSTNAME=models.CharField(max_length=20,unique=True,null=False,blank=False) 
    IP=models.CharField(max_length=20,null=True,blank=True)
    TIPO= models.CharField(max_length=20,choices=TIPO_SERVER,default=1,null=False,blank=False)
    SISTEMA_OPERATIVO= models.CharField(max_length=20,choices=CHOICES_SO,default=1,null=False,blank=False)
    PROCESADOR=models.CharField(max_length=200,null=True,blank=True)
    MEMORIA_RAM=models.CharField(max_length=20,null=True,blank=True)
    ARQUITECTURA=models.CharField(max_length=20,null=True,blank=True)
    NOMBRE_COMPLETO=models.CharField(max_length=50,null=True,blank=True)
    DOMINIO=models.CharField(max_length=50,null=True,blank=True)
    APLICACIONES_INSTALADAS=models.ManyToManyField(Aplicacion)
    COMENTARIOS=models.TextField(null=True,blank=True)

    class Meta:
        verbose_name = 'Servidor'
        verbose_name_plural ='Servidores'

    def __str__(self): 
        return self.HOSTNAME
    
#--------- MODELO INTERMEDIO ( APLICACIONES - SERVIDORES ) ---
class aplicacionesServidores(models.Model):
    SERVIDOR=models.ForeignKey(servidores,on_delete=models.CASCADE)
    APLICACION=models.ForeignKey(Aplicacion,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Aplicacion'
        verbose_name_plural ='Aplicaciones instaladas' 
#-----------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------
#>>>> MODELO ROBOTS (procesos) 
class robots(models.Model):
    ACTIVO=models.BooleanField(default=False)
    NOMBRE=models.CharField(unique=True,max_length=120,null=False,blank=False)
    PRODUCCION = models.ForeignKey(servidores,null=True, on_delete=models.PROTECT, related_name='robots_produccion', limit_choices_to={'TIPO': 'Produccion'})
    TEST = models.ForeignKey(servidores,null=True, on_delete=models.PROTECT, related_name='robots_test', limit_choices_to={'TIPO': 'Test'})
    DESARROLLO = models.ForeignKey(servidores,null=True, on_delete=models.PROTECT, related_name='robots_desarrollo', limit_choices_to={'TIPO': 'Desarrollo'})
    FECHA_PUESTA_PRD=models.DateField(null=True,blank=True)
    GERENCIA=models.ForeignKey(Gerencia,on_delete=models.PROTECT,blank=False,null=False)
    USUARIO=models.ForeignKey(Usuario,on_delete=models.PROTECT,blank=False,null=False)
    PROVEEDOR=models.ForeignKey(Proveedor,on_delete=models.PROTECT,blank=True,null=True,verbose_name="DESARROLLADOR")
    ATENDIDO=models.CharField(max_length=11,choices=ATENDIDO_DESATENDIDO,default="ATENDIDO",null=False,blank=False)
    ULTIMO_PAQUETE=models.CharField(max_length=20,null=True,blank=True)
    ULTIMA_ACTUALIZACION=models.DateField(null=True,blank=True)
    ARCHIVO_CONFIG=models.CharField(max_length=255,null=False,blank=False)
    RUTAS_INPUT=models.CharField(max_length=255,null=True,blank=True)
    RUTAS_OUTPUT=models.CharField(max_length=255,null=True,blank=True)
    DESCRIPCION_BREVE=models.TextField(null=True,blank=True)
    APLICACIONES_USADAS=models.ManyToManyField(Aplicacion)
    COMENTARIOS=models.TextField(null=True,blank=True)
    EJECUCIONES=models.IntegerField(null=True,blank=True)
    ERRORES=models.IntegerField(null=True,blank=True)
    FATAL=models.IntegerField(null=True,blank=True)
    REPROCESAR=models.TextField(null=True,blank=True)
    
    class Meta:
        verbose_name = 'Robot'
        verbose_name_plural ='Robots'

    def __str__(self):
        return self.NOMBRE

#--------- MODELS INTERMEDIARIOS --

class aplicacionesRobot(models.Model):
    ROBOT=models.ForeignKey(robots,on_delete=models.CASCADE)
    APLICACION=models.ForeignKey(Aplicacion,on_delete=models.CASCADE)

    
    class Meta:
        verbose_name = 'Aplicacion'
        verbose_name_plural ='Aplicaciones utilizadas' 
    


class reprocesoRobot(models.Model):
    ROBOT=models.ForeignKey(robots,on_delete=models.CASCADE)
    REPROCESAR=models.TextField(verbose_name="DETALLE")


    class Meta:
        verbose_name = 'Paso'
        verbose_name_plural ='Pasos para reprocesar' 

    def __str__(self):
        return "Paso"

#-----------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------
#>>>> MODELO EJECUCIONES 
class ejecucionesProcesos(models.Model):
    SERVIDOR=models.ForeignKey(servidores,on_delete=models.PROTECT,null=False,blank=True)
    ROBOT=models.ForeignKey(robots,on_delete=models.PROTECT,null=False,blank=False)
    TIPO_EJECUCION=models.CharField(max_length=20,choices=PERIODICIDAD,default="Diario",null=False,blank=False)

    DOM=models.BooleanField(default=False)
    LUN=models.BooleanField(default=False)
    MAR=models.BooleanField(default=False)
    MIE=models.BooleanField(default=False)
    JUE=models.BooleanField(default=False)
    VIE=models.BooleanField(default=False)
    SAB=models.BooleanField(default=False)

    CANTIDAD_EJECUCIONES_MENSUALES = models.IntegerField(null=True,blank=True,default=0)
    ESPACIO_AGENDA_MIN=models.IntegerField(verbose_name="MINUTOS RESERVADOS EN AGENDA",null=True,blank=True,default=15)
    EJECUCIONES_ACUMULADO=models.BigIntegerField(verbose_name="ACUM. EJECUCIONES (30 dias)",null=True,blank=True)
    DURACION_TAREA_MINUTOS_MANUAL=models.IntegerField(verbose_name="DURACION DE LA TAREA (manualmente) Min.",null=True,blank=False)
    DURACION_MENSUAL=models.IntegerField(verbose_name="HS LABORABLES MENSUALES",null=True,blank=False)
    TIPO_ESFUERZO=models.CharField(max_length=10,choices=TIPO_ESFUERZO,default="Medio",null=False,blank=False)
    FTE=models.DecimalField(verbose_name="FTE",max_digits=10,decimal_places=2,null=True,blank=True,default=0)
    CONSUMO_TOTAL =models.DecimalField(max_digits=5,verbose_name="TOTAL HORAS AGENDA (mensual)",decimal_places=2,null=True,blank=True,default=0)
    COMENTARIOS=models.TextField(null=True,blank=True)
    FECHA_INICIO =  models.DateField(null=True,blank=True)
    HORA_INICIO_EJECUCION = models.TimeField(null=True,blank=True)
    HORA_FIN_CALCULADA = models.TimeField(null=True,blank=True)
    LISTA=models.TextField(null=True,blank=True)

    class Meta:
        verbose_name = 'Ejecucion'
        verbose_name_plural ='Ejecuciones'

    def __str__(self): 
        texto = str(self.ROBOT)
        return texto
                                    
    def save(self, *args, **kwargs): #ESTE METODO REESCRIBE EL "GUARDADO" DE LA TABLA.(podemos disparar func. desde este método)
        
        hora_inicio = self.HORA_INICIO_EJECUCION
        minutos = self.ESPACIO_AGENDA_MIN
        hora_fin = datetime.now().replace(hour=hora_inicio.hour, minute=hora_inicio.minute) + timedelta(minutes=minutos)
        self.HORA_FIN_CALCULADA = hora_fin


        self.SERVIDOR = self.ROBOT.SERVIDOR
        
        cant = 0

        if self.TIPO_EJECUCION =="Diario":

            if self.DOM==True:
                cant += 1

            if self.LUN==True:
                cant += 1

            if self.MAR==True:
                cant += 1

            if self.MIE==True:
                cant += 1

            if self.JUE==True:
                cant += 1

            if self.VIE==True:
                cant += 1

            if self.SAB==True:
                cant += 1

        if self.TIPO_EJECUCION=="Diario":   
            self.CANTIDAD_EJECUCIONES_MENSUALES =  cant * 4 + 2
        elif self.TIPO_EJECUCION=="Quincenal":
            self.CANTIDAD_EJECUCIONES_MENSUALES = 2
        elif self.TIPO_EJECUCION=="Mensual":
            self.CANTIDAD_EJECUCIONES_MENSUALES = 1
        else:
            self.CANTIDAD_EJECUCIONES_MENSUALES = 0
        
        CONSUM = self.CANTIDAD_EJECUCIONES_MENSUALES * self.ESPACIO_AGENDA_MIN

        if CONSUM > 0:
            self.CONSUMO_TOTAL = CONSUM / 60

        self.FTE = self.CONSUMO_TOTAL / self.DURACION_MENSUAL

        lista = []

        if self.DOM == True:
            lista.append("DOM")
        
        if self.LUN == True:
            lista.append("LUN")

        if self.MAR == True:
            lista.append("MAR")

        if self.MIE == True:
            lista.append("MIE")

        if self.JUE == True:
            lista.append("JUE")

        if self.VIE == True:
            lista.append("VIE")

        if self.SAB == True:
            lista.append("SAB")

        self.LISTA = lista

        super(ejecucionesProcesos, self).save(*args, **kwargs)
#-----------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------
#>>>> MODELO INCIDENTES
class incidencias(models.Model):
    ESTADO=models.CharField(max_length=30,choices=ESTADO_INCIDENCIAS,default="Recibido",null=True,blank=True)
    N_INCIDENTE=models.IntegerField(blank=False,null=False,unique=True)
    ROBOT=models.ForeignKey(robots,on_delete=models.CASCADE,null=False,blank=False)
    NOMBRE_INDICENCIA=models.CharField(max_length=100,null=False,blank=False)
    FECHA_SOLICITUD=models.DateField(null=False,blank=False)
    ASIGNADO_A=models.ForeignKey(Usuario,on_delete=models.CASCADE,blank=True,null=True)
    DESCRIPCION_INCIDENCIA=models.CharField(max_length=255,null=False,blank=False)
    DESCRIPCION_SOLUCION=models.CharField(max_length=255,null=True,blank=True)
    ULTIMA_ACTUALIZACION=models.DateField(auto_now_add=True)
    COMENTARIOS=models.TextField(null=True,blank=True)
    
    class Meta:
        verbose_name = 'Incidente'
        verbose_name_plural ='Incidentes'


    def clean(self):
        if self.ESTADO == 'En Proceso' and self.ASIGNADO_A is None:
            raise ValidationError("Si el incidente está en curso, debe tener un asignatario.")



#>>>> MODELO MONITOREO (BASE DE DATOS DE LOS LOGS DE LOS ROBOTS)
class Monitoreo(models.Model):
    Tipo=models.TextField(null=True,blank=True)
    Fecha=models.DateField(null=True,blank=True)
    HoraEjecucion=models.TextField(null=True,blank=True)
    Proceso=models.TextField(null=True,blank=True)
    Gerencia=models.TextField(null=True,blank=True)
    Mensaje=models.TextField(null=True,blank=True)
    Duracion=models.DecimalField(max_digits=12,decimal_places=2,null=True,blank=True,verbose_name="Duracion Minutos")
    Server=models.TextField(null=True,blank=True)
    Paquete=models.TextField(null=True,blank=True)
    Comentarios=models.CharField(max_length=120,null=True,blank=True)
    clave=models.TextField(unique=True,null=True,blank=True)

    class Meta:
        verbose_name = 'Monitoreo'
        verbose_name_plural ='Monitoreos'

                                    
    def save(self, *args, **kwargs): 
        
        Robots = robots.objects.all()
        
        for proceso in Robots:
            if str(proceso.NOMBRE) == str(self.Proceso):
                self.Gerencia = proceso.GERENCIA.GERENCIA

        super(Monitoreo, self).save(*args, **kwargs)

#>>>> MODELO MONITOREO (BASE DE DATOS DE LOS LOGS DE LOS ROBOTS)
class Tarea(models.Model):
    ESTADO_CSS = {
        "No inciado": "estado-no-iniciado",
        "inciado": "estado-iniciado",
        "Esperando Respuesta": "estado-esperando",
        "Finalizada": "estado-finalizada",
    }

    ROBOT_ASOCIADO = models.ForeignKey(robots,on_delete=models.CASCADE,blank=True,null=True)
    NOMBRE = models.TextField(null=False,blank=False)
    FECHA_INICIO = models.DateField(null=True,blank=True)
    FECHA_FIN = models.DateField(null=True,blank=True)
    TIEMPO_INVERTIDO = models.TimeField(default=timedelta(minutes=30), null=True, blank=True)
    ESTADO = models.CharField(max_length=30,choices=ESTADO_TAREAS,default="No inciado",null=False,blank=False)
    GERENCIA_A_IMPUTAR = models.CharField(max_length=255,blank=True,null=True)
    COMENTARIOS=models.TextField(null=True,blank=True)

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'  

    def __str__(self):
        return self.NOMBRE
    
                                        
    def save(self, *args, **kwargs): 
        
        if self.ROBOT_ASOCIADO:
            self.GERENCIA_A_IMPUTAR=self.ROBOT_ASOCIADO.GERENCIA.GERENCIA
        super(Tarea, self).save(*args, **kwargs)  
    
    def class_css(self):
        return self.ESTADO_CSS.get(self.ESTADO, "")