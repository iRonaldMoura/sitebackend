from django.urls import path
from principal.views.blogpostView import blogpost


urlpatterns = [
    path('blog-post/',blogpost, name='blog-post'),

]