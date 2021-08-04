from django.shortcuts import render, get_object_or_404
from .models import Publicacao



def publicacao_lista(request):
 publicacoes = Publicacao.objects.all()
 return render(request,
 'blog/publicacao/lista.html',
 {'publicacoes': publicacoes})

def publicacao_detalhe(request, year, month, day, publicacao):
    publicacao = get_object_or_404(Publicacao, 
    slug=publicacao,
    situacao='publicado',
    publicado_em__year=year,
    publicado_em__month=month,
    publicado_em__day=day)
    return render(request,'blog/publicacao/detalhe.html',{'publicacao': publicacao})
