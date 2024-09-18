from django.db import models

# Create your models here.
class Marca(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Carro(models.Model):
    descricao = models.CharField(max_length=200)
    modelo = models.TextField()
    cor = models.CharField(max_length=100)
    ano = models.IntegerField()
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao