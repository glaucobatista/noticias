from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
 path('', views.publicacao_lista, name='publicacao_lista'),
 path('<int:year>/<int:month>/<int:day>/<slug:publicacao>/',
 views.publicacao_detalhe,
 name='publicacao_detalhe'),
]