from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_photographer = models.BooleanField(default=False)  # Indica se é fotógrafo

    def __str__(self):
        return f"{self.user.username} - {'Fotógrafo' if self.is_photographer else 'Usuário Comum'}"
    