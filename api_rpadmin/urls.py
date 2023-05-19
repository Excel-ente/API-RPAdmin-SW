
from django.contrib import admin
from django.urls import path,include,re_path

from Api.router import router_post


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(

   openapi.Info(
      title="RPAdmin",
      default_version='v2.0.0',
      description="Sistema de gestion de procesos y servidores RPA.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include(router_post.urls)),
    path('', admin.site.urls),
]
