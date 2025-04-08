from django.urls import path
from principal.views.contactView import contact


urlpatterns = [
    
    path('contact/', contact, name='contact'),
]