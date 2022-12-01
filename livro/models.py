from pickle import TRUE
from tabnanny import verbose
from django.db import models
from datetime import date
from usuario.models import Usuario


# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)

    class Meta():
        verbose_name = 'Categoria'


    def __str__(self) -> str:
        return self.nome


class Livro(models.Model):
    nome = models.CharField(max_length = 60)
    autor = models.CharField(max_length = 30)
    co_autor = models.CharField(max_length = 30, blank = True)
    editora = models.CharField(max_length = 30)
    data_cadastro = models.DateField(default=date.today)
    emprestado = models.BooleanField(default = False)
    nome_emprestado = models.CharField(max_length = 30, blank= True)
    data_emprestimo = models.DateTimeField(blank = True, null = True)
    data_devolucao = models.DateField(blank = True, null = True)
    tempo_duracao = models.DateField(blank = True, null = True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    class Meta():
        verbose_name='Livro'

    def __str__(self) -> str:
        return self.nome


class Emprestimo():
    pass 

    