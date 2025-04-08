
from django.shortcuts import render
from django.http import HttpResponse




def portfolio_item (request):
    
    if request.method == 'GET':
        return render(request, 'portfolio-item.html')