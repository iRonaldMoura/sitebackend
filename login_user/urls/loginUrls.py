from django.urls import path
from login_user.views.loginView import login_register_view
from login_user.views.logoutView import logout_view  # Importe a view de logout

urlpatterns = [
    path("login/", login_register_view, name="login"),  # Rota para o login
    path("login/<int:id>/", login_register_view, name="login-user"),  # Rota para o login com ID
    path("logout/", logout_view, name="logout"),  # Rota para o logout
]