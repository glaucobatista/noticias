from django.contrib import admin

from .models import Publicacao, Comentario

@admin.register(Publicacao)
class PublicacaoAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor','publicado_em','situacao')
    list_filter = ('situacao', 'criado_em', 'publicado_em', 'autor')
    search_fields = ('titulo', 'descricao')
    prepopulated_fields = {'slug': ('titulo',)}
    raw_id_fields = ('autor',)
    date_hierarchy = 'publicado_em'
    ordering = ('situacao', 'publicado_em')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'publicacao', 'criado_em', 'ativo',)
    list_filter = ('ativo', 'criado_em', 'atualizado_em',)
    search_fields = ('nome', 'email', 'descricao')