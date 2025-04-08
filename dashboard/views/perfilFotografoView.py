from django.shortcuts import render
from django.http import HttpResponse





def perfil_fotografo (request):
    
    if request.method == 'GET':
        return render(request, 'perfil-fotografo.html')