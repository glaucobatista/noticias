from django.contrib.sitemaps import Sitemap
from .models import Publicacao


class PublicacaoSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    def items(self):
        return Publicacao.objects.all()
    def lastmod(self, obj):
        return obj.atualizado_em