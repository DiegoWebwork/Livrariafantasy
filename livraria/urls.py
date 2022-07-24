from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_livros, name='listar_livros'),
    path('listar_categorias', views.listar_categorias, name='listar_categorias'),
    path('listar_autores', views.listar_autores, name='listar_autores'),
]