from django import forms
from livraria.models import Livro


class LivroForm(forms.ModelForm):

    class Meta:
        model = Livro
        fields = ('nome', 'autor', 'categoria', 'codigo',
        'quantidade', 'valor', 'imagem', 'ano', 'descricao')

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder':'Nome do Livro'}),
            'autor': forms.SelectMultiple(attrs={'class': 'form-control',
                                            'placeholder':'Nome do Autor'}),
            'categoria': forms.Select(attrs={'class': 'form-control',
                                              'placeholder':'Nome do Categoria'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control',
                                              'placeholder':'O codigo do produto'}),
            'quantidade': forms.TextInput(attrs={'class': 'form-control'}),
            'valor': forms.TextInput(attrs={'class': 'form-control'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
            'ano': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder':'Ano de lançamento'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control',
                                                'placeholder':'escreve aqui uma breve descrição'}),
        }