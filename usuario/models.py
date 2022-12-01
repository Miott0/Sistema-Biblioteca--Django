from django.db import models

# Create your models here.

#miotterafael@gmail.com 1234567

class Usuario(models.Model):
    nome = models.CharField(max_length = 40)
    email = models.EmailField()
    senha = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.nome
