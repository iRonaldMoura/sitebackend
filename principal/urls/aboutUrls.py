from django.urls import path
from principal.views.aboutView import about


urlpatterns = [
    path('about/',about, name='about'),

]