from django.urls import path
from login_user.views.redefinirView import redefinir


urlpatterns = [
    path('redefinir/',redefinir, name='redefinir'),
   
]