from django.urls import path
from pacotes.views.pricingView import pricing


urlpatterns = [
    path('pricing/',pricing, name='pricing'),
   
]