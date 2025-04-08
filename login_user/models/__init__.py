from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

ROLE_CHOICE = (
    (1, 'Admin'),
    (2, 'Fotografo'),
    (3, 'Usuario')
)


from .Perfil import Perfil
from .Avaliacao import Avaliacao
from .DiaSemana import DiaSemana
from .Estado import Estado
from .Cidade import Cidade
from .Bairro import Bairro
from .Endereco import Endereco
from .Especialidade import Especialidade
from .user_profile import UserProfile
