from django.http import HttpResponse
from django.shortcuts import render

def bloghome (request):
    
    if request.method == 'GET':
        return render(request, 'blog-home.html')