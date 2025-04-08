from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from login_user.models import UserProfile
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.exceptions import ValidationError as DjangoValidationError

def registro(request):
    if request.method == "POST":
        try:
            # Coleta os dados do formulário
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            password = request.POST.get("password")
            confirm_password = request.POST.get("password2")  # Confirmação de senha
            is_photographer = request.POST.get("is_photographer") == "on"

            # Validações
            if not email or not password or not confirm_password:
                raise ValidationError("Todos os campos são obrigatórios.")

            if password != confirm_password:
                raise ValidationError("As senhas não coincidem.")

            try:
                validate_email(email)  # Valida o formato do e-mail
            except DjangoValidationError:
                raise ValidationError("Por favor, insira um e-mail válido.")

            if User.objects.filter(email=email).exists():
                raise ValidationError("Este e-mail já está em uso.")

            # Cria o usuário
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            # Cria o perfil do usuário
            UserProfile.objects.create(user=user, is_photographer=is_photographer)

            # Mensagem de sucesso e redirecionamento
            messages.success(request, "Cadastro realizado com sucesso! Faça login para continuar.")
            return redirect("login")  # Redireciona para a página de login

        except ValidationError as e:
            messages.error(request, str(e))
        except Exception as e:
            messages.error(request, "Ocorreu um erro durante o cadastro. Tente novamente.")
        
        # Renderiza o template de registro novamente em caso de erro
        return render(request, "registro.html")

    # Renderiza o template de registro para requisições GET
    return render(request, "registro.html")