from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

#swagger
from rest_framework_swagger.views import get_swagger_view

# JWT Access/Refresh tokens
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)






schema_view = get_swagger_view(title='Kutubxona API', url='/v1/')

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('home/', views.home_page, name='home_page'),
    path("users/", include("users.urls", namespace="users")),
    path("books/", include("books.urls", namespace="books")),

    path('admin/', admin.site.urls),


    # path('swagger/', schema_view), #swagger UI
    path("api/", include("api.urls", namespace="kutubxona_api")),
    path('api-auth/', include('rest_framework.urls', namespace="rest_framework")),   # rest_frameworkdan authendication(o'ng burchakda) qilish uchun
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # JWT Access token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # JWT Refresh token
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)