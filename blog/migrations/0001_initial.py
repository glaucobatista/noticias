# Generated by Django 3.0 on 2021-08-04 02:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publicado_em')),
                ('descricao', models.TextField()),
                ('publicado_em', models.DateTimeField(default=django.utils.timezone.now)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('situacao', models.CharField(choices=[('rascunho', 'Rascunho'), ('publicado', 'Publicado')], default='rascunho', max_length=10)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publicacoes_blog', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-publicado_em',),
            },
        ),
    ]
