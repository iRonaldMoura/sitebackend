# principal/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),  # URL da página inicial
]
