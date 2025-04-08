
from login_user.models import *

class Cidade(models.Model):
    estado = models.ForeignKey(Estado, null=True, related_name='estado', on_delete=models.SET_NULL)
    nome = models.CharField(null=False, max_length=20)
    status = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.nome, self.estado.nome)
