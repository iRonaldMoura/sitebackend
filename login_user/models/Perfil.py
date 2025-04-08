from login_user.models import *
from django.db.models import Sum, Count


class Perfil(models.Model): 
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cargo = models.IntegerField(choices=ROLE_CHOICE, default=3)
    data_nascimento = models.DateField(default=None, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    favoritos = models.ManyToManyField(User, blank=True, related_name='favoritos')
    Endereços = models.ManyToManyField("Endereco", blank=True, related_name='endereços')
    

    
    
    def __str__(self):
        return '{}'.format(self.usuario.username)

    @receiver(post_save, sender=User)
    def criar_perfil_usuario(sender, instance, created, **kwargs):
        try:
            if created:
                Perfil.objects.create(usuario=instance)
        except:
            pass

    @receiver(post_save, sender=User)
    def salvar_perfil_usuario(sender, instance, **kwargs):
        try:
            instance.perfil.save()
        except:
            pass
