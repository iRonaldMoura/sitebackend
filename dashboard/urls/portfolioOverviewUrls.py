
from django.urls import path
from dashboard.views.portfolioOverviewView import portfolio_overview






urlpatterns = [
    path('portfolio-overview/', portfolio_overview, name='portfolio-overview'),
   
]