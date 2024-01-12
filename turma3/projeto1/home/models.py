from django.db import models

class Livraria(models.Model):
    nome_livro = models.CharField(max_length=100)
    ano_da_publicacao = models.IntegerField(max_length=4)
    quantidade_pagina = models.IntegerField(max_length=100)
    nome_autor = models.CharField(max_length=500)
    nome_editora = models.CharField(max_length=500)
    preco = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return self.nome_livro