from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse


def redefinir (request):
    
    if request.method == 'GET':
        return render(request, 'redefinir.html')