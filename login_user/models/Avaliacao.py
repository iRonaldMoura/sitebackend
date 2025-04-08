from login_user.models import *


class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, related_name='avaliou', on_delete=models.CASCADE)
    avaliado = models.ForeignKey(User, related_name='avaliado', on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    opiniao = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True, null=True)
    atualizado_em = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return 'usuario: {} | Avaliado: {}'.format(self.usuario.first_name, self.avaliado.first_name)

