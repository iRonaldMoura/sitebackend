from django.http import HttpResponse
from django.shortcuts import render

def contact (request):
    
    if request.method == 'GET':
        return render(request, 'contact.html')