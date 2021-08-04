from django.shortcuts import render, get_object_or_404
from .models import Publicacao



def publicacao_lista(request):
 publicacoes = Publicacao.objects.all()
 return render(request,
 'blog/publicacao/lista.html',
 {'publicacoes': publicacoes})

def publicacao_detalhe(request, year, month, day, publicacao):
    publicacao = get_object_or_404(Publicacao, slug=publicado_em,
    situacao='publicado',
    publish__year=year,
    publish__month=month,
    publish__day=day)
    return render(request,
    'blog/publicacao/detail.html',
    {'publicacao': publicacao})
