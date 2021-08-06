from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe 
import markdown
from ..models import Publicacao

register = template.Library()
@register.simple_tag
def total_publicacoes():
     return Publicacao.objects.count()

@register.inclusion_tag('blog/publicacao/ultimas_publicacoes.html')
def mostrar_ultimas_publicacoes(count=5):
    ultimas_publicacoes = Publicacao.objects.order_by('-publicado_em')[:count]
    return {'ultimas_publicacoes': ultimas_publicacoes}

@register.simple_tag
def buscar_publicacoes_mais_comentadas(count=2):
    return Publicacao.objects.annotate(total_comentarios=Count('comentarios')
    ).order_by('-total_comentarios')[:count]

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))