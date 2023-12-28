from django.db import models

class comments(models.Model):
    nome = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    ano_criacao = models.IntegerField()
    def __str__(self):
        return self.nome

class todos(models.Model):
    todos = models.ForeignKey(todos, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    def __str__(self):
        return self.nome

class users(models.Model):
    users = models.ForeignKey(users, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    segundos = models.IntegerField()

    def __str__(self):
        return self.nome

class posts(models.Model):
    users = models.ForeignKey(users, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    segundos = models.IntegerField()

    def __str__(self):
        return self.nome