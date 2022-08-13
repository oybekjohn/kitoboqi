from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

#swagger
from rest_framework_swagger.views import get_swagger_view

from . import views

schema_view = get_swagger_view(title='Kutubxona API', url='/v1/')

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('home/', views.home_page, name='home_page'),
    path("users/", include("users.urls"), name="users"),
    path("books/", include("books.urls")),
    path("api/", include("api.urls")),
    path('swagger/', schema_view),

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)