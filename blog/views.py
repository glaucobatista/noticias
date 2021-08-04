from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from .models import Publicacao


class PublicacaoListView(ListView):
    queryset = Publicacao.objects.all()
    context_object_name = 'publicacoes'
    paginate_by = 1
    template_name = 'blog/publicacao/lista.html'


def publicacao_lista(request):
    object_list = Publicacao.objects.all()
    paginator = Paginator(object_list, 5) # 5 publicações por página
    page = request.GET.get('page')
    try:
        publicacoes = paginator.page(page)
    except PageNotAnInteger:
        publicacoes = paginator.page(1)
    except EmptyPage:
        publicacoes = paginator.page(paginator.num_pages)


    return render(request, 'blog/publicacao/lista.html', {'page': page,'publicacoes': publicacoes})


def publicacao_detalhe(request, year, month, day, publicacao):
    publicacao = get_object_or_404(Publicacao, 
    slug=publicacao,
    situacao='publicado',
    publicado_em__year=year,
    publicado_em__month=month,
    publicado_em__day=day)
    return render(request,'blog/publicacao/detalhe.html',{'publicacao': publicacao})
