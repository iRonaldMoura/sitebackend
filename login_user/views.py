from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)  # Realiza o logout
    return redirect("index")  # Redireciona para a página inicial (ou outra página de sua escolha)