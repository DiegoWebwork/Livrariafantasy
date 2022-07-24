from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_livros, name='listar_livros'),
    path('listar_categorias', views.listar_categorias, name='listar_categorias'),
    path('listar_autores', views.listar_autores, name='listar_autores'),
    path('livro/<int:id>/', views.detalhar_livro, name='detalhar_livro'),  # o caminho começa com livro e direciona para o id apos clicar, chamando a função detelhar_livro
    path('livro/new/', views.cadastrar_livro, name='cadastrar_livro'),
]
