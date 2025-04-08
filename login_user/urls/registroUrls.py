from django.urls import path
from login_user.views.registroView import registro



urlpatterns = [
    path('registro/',registro, name='registro'),
   
]