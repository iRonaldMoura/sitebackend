from django.urls import path
from dashboard.views.portfolioItemView import portfolio_item








urlpatterns = [
    path('portfolio-item/',portfolio_item, name='portfolio-item'),
]