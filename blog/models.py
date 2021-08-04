from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Publicacao(models.Model):
    SITUACAO_CHOICES = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
    )
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publicado_em')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publicacoes_blog')
    descricao = models.TextField()
    publicado_em = models.DateTimeField(default=timezone.now)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    situacao = models.CharField(max_length=10, choices=SITUACAO_CHOICES, default='rascunho')

    

    class Meta():
        ordering = ('-publicado_em',)
    

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('blog:publicacao_detalhe',
        args=[
        self.publicado_em.year,
        self.publicado_em.month,
        self.publicado_em.day, 
        self.slug
        ])


    

    
