from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path("users/", include("users.urls"), name="users"),
    path("books/", include("books.urls"), name="books"),

    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
