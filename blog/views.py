from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
from django.db.models import Count

from taggit.models import Tag
from .models import Publicacao, Comentario
from .forms import EnviarEmailForm, ComentarioForm

class PublicacaoListView(ListView):
    queryset = Publicacao.objects.all()
    context_object_name = 'publicacoes'
    paginate_by = 5
    template_name = 'blog/publicacao/lista.html'


def publicacao_lista(request, tag_slug=None):
    object_list = Publicacao.objects.all()
    tag = None
    
    
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    
    
    paginator = Paginator(object_list, 5) # 5 publicações por página
    page = request.GET.get('page')
    try:
        publicacoes = paginator.page(page)
    except PageNotAnInteger:
        publicacoes = paginator.page(1)
    except EmptyPage:
        publicacoes = paginator.page(paginator.num_pages)


    return render(request, 'blog/publicacao/lista.html', {'page': page,'publicacoes': publicacoes, 'tag':tag})


def publicacao_detalhe(request, year, month, day, publicacao):
    publicacao = get_object_or_404(Publicacao, 
    slug=publicacao,
    situacao='publicado',
    publicado_em__year=year,
    publicado_em__month=month,
    publicado_em__day=day)
    # Lista de Comentários ativos na publicação
    comentarios = publicacao.comentarios.filter(ativo=True)
    novo_comentario = None
    if request.method == 'POST':
        # Um comentário foi publicado
        comentario_form = ComentarioForm(data=request.POST)
        if comentario_form.is_valid():
            # Criar objeto comentário mas não salvou ainda no banco de dados
            novo_comentario = comentario_form.save(commit=False)
            # Assinar o comentário para a publicação atual
            novo_comentario.publicacao = publicacao
            # Salvar o comentário no banco de dados
            novo_comentario.save()
    else:
        comentario_form = ComentarioForm()
        print("FORMULÁRIO DE COMENTÁRIO ELSE",comentario_form)
    
    # Lista de publicações similares
    tags_ids_publicacoes = publicacao.tags.values_list('id', flat=True)
    publicacoes_similares = Publicacao.objects.filter(tags__in=tags_ids_publicacoes).exclude(id=publicacao.id)
    publicacoes_similares = publicacoes_similares.annotate(same_tags=Count('tags')).order_by('-same_tags','-publicado_em')[:4]

    return render(request,'blog/publicacao/detalhe.html',
            {'publicacao': publicacao,'comentarios':comentarios, 
            'novo_comentario':novo_comentario, 
            'comentario_form':comentario_form, 
            'publicacoes_similares':publicacoes_similares})


def compartilhar_publicacao(request, publicacao_id):
    publicacao = get_object_or_404(Publicacao, id=publicacao_id, situacao='publicado')
    sent = False

    if request.method == 'POST':
     # Form foi submetido
        form = EnviarEmailForm(request.POST)
        if form.is_valid():
            # Os campos do form foram validados
            cd = form.cleaned_data
            # ... enviando email
            publicacao_url = request.build_absolute_uri(
            publicacao.get_absolute_url())
            subject = f"{cd['nome']} recomenda a leitura de " \
            f"{publicacao.titulo}"
            message = f"Read {publicacao.titulo} em {publicacao_url}\n\n" \
            f"{cd['nome']}\'s comentario: {cd['comentario']}"
            send_mail(subject, message, 'glaucogti@gmail.com',
            [cd['para']])
            sent = True
    else:
        form = EnviarEmailForm()
        print ("FORMULARIO EMAIL", form)
    return render(request, 'blog/publicacao/compartilhar.html', 
    {'publicacao': publicacao,'form': form, 'sent':sent})