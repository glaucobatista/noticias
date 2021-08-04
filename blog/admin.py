from django.contrib import admin

from .models import Publicacao

@admin.register(Publicacao)
class PublicacaoAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor','publicado_em','situacao')
    list_filter = ('situacao', 'criado_em', 'publicado_em', 'autor')
    search_fields = ('titulo', 'descricao')
    prepopulated_fields = {'slug': ('titulo',)}
    raw_id_fields = ('autor',)
    date_hierarchy = 'publicado_em'
    ordering = ('situacao', 'publicado_em')