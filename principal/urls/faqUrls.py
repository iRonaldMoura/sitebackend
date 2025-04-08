from django.urls import path
from principal.views.faqView import faq


urlpatterns = [
    path('faq/', faq, name='faq'),
]