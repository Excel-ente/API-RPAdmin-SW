
# ---------------------------------------------------------------------------------------------------------
#   Proyecto RPAdmin 2.0.0   2023
#
#   Desarrollador: Kevin Turkienich
# ---------------------------------------------------------------------------------------------------------

# Importacion de librerias
# ---------------------------------------------------------------------------------------------------------

#Librerias de rest_framework
from rest_framework.routers import DefaultRouter


#Importaciones de modulos internos
from Api.views import ServidorModelViewSet,RobotModelViewSet

# --------------------------------------------------------------------------------------------------------

router_post = DefaultRouter()
router_post.register(r'servidores', ServidorModelViewSet, basename='servers')
router_post.register(r'robots', RobotModelViewSet, basename='robots')

