from login_user.models import *


class Endereco(models.Model):
    bairro = models.ForeignKey(Bairro, null=True, related_name='bairro', on_delete=models.SET_NULL)
    nome = models.CharField(null=False, max_length=100)
    endereco = models.CharField(null=False, max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=7)
    longitude = models.DecimalField(max_digits=9, decimal_places=7)
    hora_abertura = models.TimeField()
    hora_fechamento = models.TimeField()
    dias_semana = models.ManyToManyField(DiaSemana, blank=True, related_name='dias_semana')
    telefone = models.CharField(null=True, blank=True, max_length=50)
    status = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.nome)
