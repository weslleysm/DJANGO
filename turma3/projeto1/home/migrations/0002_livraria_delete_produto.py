# Generated by Django 5.0.1 on 2024-01-11 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livraria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_livro', models.CharField(max_length=100)),
                ('ano_da_publicacao', models.IntegerField(max_length=4)),
                ('quantidade_pagina', models.IntegerField(max_length=100)),
                ('nome_autor', models.CharField(max_length=500)),
                ('nome_editora', models.CharField(max_length=500)),
                ('preco', models.FloatField(default=0.0)),
            ],
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
    ]