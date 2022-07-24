# Generated by Django 4.0.6 on 2022-07-24 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('codigo', models.CharField(max_length=20)),
                ('quantidade', models.IntegerField()),
                ('valor', models.FloatField()),
                ('imagem', models.ImageField(blank=True, upload_to='livraria/media')),
                ('ano', models.IntegerField()),
                ('descricao', models.TextField()),
                ('autor', models.ManyToManyField(blank=True, to='livraria.autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livraria.categoria', verbose_name='Categoria')),
            ],
        ),
    ]