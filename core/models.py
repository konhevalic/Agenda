from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100) #no maximo 100caracteres
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True) #insere a hora atual em que foi criado o evento
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.titulo