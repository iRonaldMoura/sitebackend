
from django.urls import path
from dashboard.views.perfilFotografoView import perfil_fotografo




urlpatterns = [
    path('perfil-fotografo/',perfil_fotografo, name='perfil-fotografo'),
]