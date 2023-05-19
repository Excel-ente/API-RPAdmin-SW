# ---------------------------------------------------------------------------------------------------------
#   Proyecto RPAdmin 2.0.0   2023
#
#   Desarrollador: Kevin Turkienich
# ---------------------------------------------------------------------------------------------------------

# Importacion de librerias
# ---------------------------------------------------------------------------------------------------------

#Librerias de rest_framework
from rest_framework.serializers import ModelSerializer

#Importaciones de modulos internos
from administracion.models import servidores,robots
# ---------------------------------------------------------------------------------------------------------

# Serializadores

class ServidorSerializer(ModelSerializer):
    class Meta:
        model = servidores
        fields = ['HOSTNAME','IP','TIPO','SISTEMA_OPERATIVO','PROCESADOR','MEMORIA_RAM','ARQUITECTURA']

class RobotSerializer(ModelSerializer):
    class Meta:
        model = robots
        fields = ['NOMBRE','PRODUCCION','DESARROLLO','TEST','ACTIVO','FECHA_PUESTA_PRD','GERENCIA','USUARIO','ATENDIDO','ULTIMO_PAQUETE','ARCHIVO_CONFIG','RUTAS_INPUT','RUTAS_OUTPUT','EJECUCIONES','FATAL','APLICACIONES_USADAS']


# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------