# ---------------------------------------------------------------------------------------------------------
#   Proyecto RPAdmin 2.0.0   2023
#
#   Desarrollador: Kevin Turkienich
# ---------------------------------------------------------------------------------------------------------

# Importacion de librerias
# ---------------------------------------------------------------------------------------------------------

#Librerias de rest_framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

#Importaciones de modulos internos
from administracion.models import servidores,robots
from Api.serializers import ServidorSerializer,RobotSerializer

# ---------------------------------------------------------------------------------------------------------


class ServidorModelViewSet(ModelViewSet):
    permission_classes=[IsAuthenticated]
    serializer_class=ServidorSerializer
    queryset=servidores.objects.all()

class RobotModelViewSet(ModelViewSet):
    permission_classes=[IsAuthenticated]
    serializer_class=RobotSerializer
    queryset=robots.objects.all()