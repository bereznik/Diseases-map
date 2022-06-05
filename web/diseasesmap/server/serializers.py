from rest_framework import serializers
from server.models import Localidades,Notificacoes,Doencas,Usuarios

class LocalidadesSerializers(serializers.ModelSerializer):
    class Meta:
        model=Localidades
        fields=('id','estado','cidade','latitude','longitude')

class NotificacoesSerializers(serializers.ModelSerializer):
    class Meta:
        model=Notificacoes
        fields=('id','idmunicipio','iddoenca','casos')

class DoencasSerializers(serializers.ModelSerializer):
    class Meta:
        model=Doencas
        fields=('id','nome','descricao','vacinadisp','link')

class UsuariosSerializers(serializers.ModelSerializer):
    class Meta:
        model=Usuarios
        fields=('id','posto','nome','nomeguerra','email','senha','om','foto')