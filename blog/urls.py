from django.urls import path

from . import views
app_name = 'blog'

urlpatterns = [
 path('', views.publicacao_lista, name='publicacao_lista'),
#  path('', views.PublicacaoListView.as_view(), name='publicacao_lista'),
 path('<int:year>/<int:month>/<int:day>/<slug:publicacao>/', views.publicacao_detalhe, name='publicacao_detalhe'),
 path('<int:publicacao_id>/compartilhar/', views.compartilhar_publicacao, name='compartilhar_publicacao'),
 path('tag/<slug:tag_slug>/',views.publicacao_lista, name='publicacoes_por_tag'),
 
]