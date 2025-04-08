from django.shortcuts import render
from django.http import HttpResponse


def pricing (request):
    
    if request.method == 'GET':
        return render(request, 'pricing.html')

