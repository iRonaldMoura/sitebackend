from django.contrib import admin
from.models import *


# este campo refere-se a area administrativa do django
class PerfilAdmin(admin.ModelAdmin): 
    list_display = ('usuario','cargo','data_nascimento',) #Adiciona campos na Area Admin 
    empty_value_display = 'Vazio' # escreve Vazio caso o campo não seja preenchido 
    list_display_links  = ('usuario','cargo','data_nascimento',) #Cria Links sobre o itens mencionados 
    list_filter = ('usuario','cargo','data_nascimento',) #permite que criemos um filtro de dados baseados em camposss
    fields = ('usuario','cargo',) #permite dizer quais campos serão exibidos no formularios e quais não serao
    exclude = ('favoritos',) #Ele removerá do formulario os campos que forem adcionados
    readonly_fields = ('usuario',) #deixa o campo apenas como leitura no formulario de edição e criação, faremos isso aqui para que nao seja permitido alterar o usuario atrelado a este perfil 
    search_fields = ('usuario__username',) #lista de campos que poderao ser pesquisados na tela de listagem do admin
    
class PerfilAdmin(admin.ModelAdmin):
        fieldsets = (
            ('Usuario', {
                'fields': ('usuario', 'data_nascimento', 'image'),
            }),
            
    )   




































admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Especialidade)
admin.site.register(Avaliacao)
admin.site.register(DiaSemana)
admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Bairro)
admin.site.register(Endereco)