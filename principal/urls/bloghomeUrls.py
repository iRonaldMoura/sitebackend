from django.urls import path
from principal.views.bloghomeView import bloghome


urlpatterns = [
    path('blog-home/',bloghome, name='blog-home'),

]