from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from login_user.models import UserProfile

def login_register_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        # Autentica o usuário
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            
            # Verifica se o usuário é um fotógrafo ou cliente
            try:
                user_profile = UserProfile.objects.get(user=user)
                if user_profile.is_photographer:
                    messages.success(request, "Login realizado com sucesso! Bem-vindo, fotógrafo.")
                else:
                    messages.success(request, "Login realizado com sucesso! Bem-vindo, cliente.")
            except UserProfile.DoesNotExist:
                messages.success(request, "Login realizado com sucesso!")
            
            # Redireciona para a página inicial (index)
            return redirect("index")  # Redireciona para a página inicial

        else:
            messages.error(request, "E-mail ou senha incorretos.")
    
    return render(request, "login.html")