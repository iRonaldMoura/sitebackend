from django.http import HttpResponse
from django.shortcuts import render

def faq (request):
    
    if request.method == 'GET':
        return render(request, 'faq.html')