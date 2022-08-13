from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

# Swagger UI
from rest_framework import permissions
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from drf_yasg import openapi

# JWT Access/Refresh tokens
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


# Swagger UI sxemasi
schema_view = swagger_get_schema_view(
   openapi.Info(
      title="Kutubxona API",
      default_version='1.0.0',
      description="Kutubxona projecti uchun API",
      contact=openapi.Contact(email='oybeksjob@gmail.com'),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('home/', views.home_page, name='home_page'),
    path("users/", include("users.urls", namespace="users")),
    path("books/", include("books.urls", namespace="books")),


    path('api/v1/', 
    include([
        path('admin/', admin.site.urls),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),  #swagger UI

        # bular swaggerni ichida tursa swaggerda korinadi
        path("api/", include("api.urls", namespace="kutubxona_api")),
        path('api-auth/', include('rest_framework.urls', namespace="rest_framework")),      # rest_frameworkdan authendication(o'ng burchakda) qilish uchun
        path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),        # JWT Access token
        path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),       # JWT Refresh token

        # path('api/token/verify/', views.verify_jwt_token, name='token_verify'),           # JWT token verify  # bu qismi qo'shish kerak 
        ])
    ),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)