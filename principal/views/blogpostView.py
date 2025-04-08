from django.http import HttpResponse
from django.shortcuts import render

def blogpost (request):
    
    if request.method == 'GET':
        return render(request, 'blog-post.html')