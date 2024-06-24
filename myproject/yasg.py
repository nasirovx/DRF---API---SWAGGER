from django.urls import path 
from rest_framework import permissions
from drf_yasg import openapi 
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='Django Movie',
        default_version = 'v1',
        description="API documentation for Movies",
        license=openapi.License(name="BSD License"), 
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger(?P<format>\.json|\.yaml)', schema_view.with_ui(cache_timeout=0), name='schema-swagger-ui'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
