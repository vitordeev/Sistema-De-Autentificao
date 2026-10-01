from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=13)
    cep = models.CharField(max_length=9)
    rua = models.CharField(max_length=150)
    numero = models.CharField(max_length=4)


