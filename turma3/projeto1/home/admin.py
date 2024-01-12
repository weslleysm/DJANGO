from django.contrib import admin
from .models import Livraria

class listLivro(admin.ModelAdmin):
    list_display = ('nome_livro', 'ano_da_publicacao', 'quantidade_pagina', 'nome_autor', 'nome_editora', 'preco')

admin.site.register(Livraria, listLivro)
