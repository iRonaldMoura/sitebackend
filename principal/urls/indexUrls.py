# principal/urls.py
from django.urls import path
from ..views import indexView

urlpatterns = [
    path('index/', indexView.index, name='index'),  # URL da página inicial
]
