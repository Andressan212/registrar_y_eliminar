# sistema_obras_sociales/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('obras/', include('obras_sociales.urls')),
]
