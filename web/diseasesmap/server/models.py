from django.db import models

# Create your models here.
class Localidades(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    estado =  models.CharField(max_length=100)
    cidade =  models.CharField(max_length=100)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

class Notificacoes(models.Model):
    id = models.AutoField(primary_key=True)
    idmunicipio = models.IntegerField()
    iddoenca = models.IntegerField()
    data = models.DateField(default=None)

class NotificacoesTotal(models.Model):
    id = models.AutoField(primary_key=True)
    idmunicipio = models.IntegerField()
    iddoenca = models.IntegerField()
    casos = models.IntegerField()

class Doencas(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao =  models.CharField(max_length=500)
    vacinadisp =  models.BooleanField(default=False)
    link = models.CharField(max_length=100)

class Usuarios(models.Model):
    class Posto(models.TextChoices):
        TENENTE = 'TEN'

    id = models.AutoField(primary_key=True)
    posto = models.CharField(max_length=100, choices=Posto.choices)
    email = models.EmailField(default=None)
    senha = models.CharField(max_length=10)
    om = models.CharField(max_length=10)
    foto = models.BinaryField()



