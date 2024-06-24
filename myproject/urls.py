from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.conf import settings
from django.conf.urls.static import static
from database.views import PersonAPIList, PersonAPIUpdate, PersonAPIDestroy
from rest_framework import permissions
from drf_yasg import openapi 
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='Django Movie',
        default_version='v1',
        description="API documentation for Movies",
        license=openapi.License(name="BSD License"), 
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('database.urls')),
    path('api/v1/people/', PersonAPIList.as_view(), name='person_api_list'),
    path('api/v1/people/<int:pk>/', PersonAPIUpdate.as_view(), name='person_api_update'),
    path('api/v1/peopledl/<int:pk>/', PersonAPIDestroy.as_view(), name='person_api_destroy'),
    
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
