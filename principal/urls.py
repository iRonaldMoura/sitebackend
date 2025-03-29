from django.urls import path
from .views import principal  # ✅ Importe a view corretamente

urlpatterns = [
    path('', principal, name='principal'),  # ✅ Defina a URL corretamente
]
