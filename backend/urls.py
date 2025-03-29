# backend/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('principal/', include('principal.urls')),  # Corrigir para a app 'principal' ou 'index'
]
