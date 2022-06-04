from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from server.models import Localidades, Notificacoes, NotificacoesTotal, Doencas, Usuarios
from server.serializers import LocalidadesSerializers, NotificacoesSerializers, NotificacoesTotalSerializers, DoencasSerializers, UsuariosSerializers

# Create your views here.

@csrf_exempt
def localidadesApi(request,pathId=0):
    if request.method=='GET':
        localidades = Localidades.objects.all()
        localidades_serializer=LocalidadesSerializers(localidades,many=True)
        return JsonResponse(localidades_serializer.data,safe=False)
    elif request.method=='POST':
        localidades_data=JSONParser().parse(request)
        localidades_serializer=LocalidadesSerializers(data=localidades_data)
        if localidades_serializer.is_valid():
            localidades_serializer.save()
            return JsonResponse("Adicionado com sucesso",safe=False)
        return JsonResponse("Falha ao adicionar", safe=False)
    elif request.method=='PUT':
        localidades_data=JSONParser().parse(request)
        localidade=Localidades.objects.get(id=localidades_data['id'])
        localidades_serializer=LocalidadesSerializers(localidade,data=localidades_data)
        if localidades_serializer.is_valid():
            localidades_serializer.save()
            return JsonResponse("Editado com sucesso",safe=False)
        return JsonResponse("Falha ao editar", safe=False)
    elif request.method=='DELETE':
        localidade=Localidades.objects.get(id=pathId)
        localidade.delete()
        return JsonResponse("Deletado com sucesso",safe=False)

def notificacoesApi(request,pathId=0):
    if request.method=='GET':
        notificacoes = Notificacoes.objects.all()
        notificacoes_serializer=NotificacoesSerializers(notificacoes,many=True)
        return JsonResponse(notificacoes_serializer.data,safe=False)
    elif request.method=='POST':
        notificacoes_data=JSONParser().parse(request)
        notificacoes_serializer=NotificacoesSerializers(data=notificacoes_data)
        if notificacoes_serializer.is_valid():
            notificacoes_serializer.save()
            return JsonResponse("Adicionado com sucesso",safe=False)
        return JsonResponse("Falha ao adicionar", safe=False)
    elif request.method=='PUT':
        notificacoes_data=JSONParser().parse(request)
        notificacao=Notificacoes.objects.get(id=notificacoes_data['id'])
        notificacoes_serializer=NotificacoesSerializers(notificacao,data=notificacoes_data)
        if notificacoes_serializer.is_valid():
            notificacoes_serializer.save()
            return JsonResponse("Editado com sucesso",safe=False)
        return JsonResponse("Falha ao editar", safe=False)
    elif request.method=='DELETE':
        notificacao=Notificacoes.objects.get(id=pathId)
        notificacao.delete()
        return JsonResponse("Deletado com sucesso",safe=False)

def notificacoesTotalApi(request,pathId=0):
    if request.method=='GET':
        notificacoesTotal = NotificacoesTotal.objects.all()
        notificacoesTotal_serializer=NotificacoesTotalSerializers(notificacoesTotal,many=True)
        return JsonResponse(notificacoesTotal_serializer.data,safe=False)
    elif request.method=='POST':
        notificacoesTotal_data=JSONParser().parse(request)
        notificacoesTotal_serializer=NotificacoesTotalSerializers(data=notificacoesTotal_data)
        if notificacoesTotal_serializer.is_valid():
            notificacoesTotal_serializer.save()
            return JsonResponse("Adicionado com sucesso",safe=False)
        return JsonResponse("Falha ao adicionar", safe=False)
    elif request.method=='PUT':
        notificacoesTotal_data=JSONParser().parse(request)
        notificacaoTotal=NotificacoesTotal.objects.get(id=notificacoesTotal_data['id'])
        notificacoesTotal_serializer=NotificacoesTotalSerializers(notificacaoTotal,data=notificacoesTotal_data)
        if notificacoesTotal_serializer.is_valid():
            notificacoesTotal_serializer.save()
            return JsonResponse("Editado com sucesso",safe=False)
        return JsonResponse("Falha ao editar", safe=False)
    elif request.method=='DELETE':
        notificacaoTotal=NotificacoesTotal.objects.get(id=pathId)
        notificacaoTotal.delete()
        return JsonResponse("Deletado com sucesso",safe=False)

def doencasApi(request,pathId=0):
    if request.method=='GET':
        doencas = Doencas.objects.all()
        doencas_serializer=DoencasSerializers(doencas,many=True)
        return JsonResponse(doencas_serializer.data,safe=False)
    elif request.method=='POST':
        doencas_data=JSONParser().parse(request)
        doencas_serializer=DoencasSerializers(data=doencas_data)
        if doencas_serializer.is_valid():
            doencas_serializer.save()
            return JsonResponse("Adicionado com sucesso",safe=False)
        return JsonResponse("Falha ao adicionar", safe=False)
    elif request.method=='PUT':
        doencas_data=JSONParser().parse(request)
        doenca=Doencas.objects.get(id=doencas_data['id'])
        doencas_serializer=DoencasSerializers(doenca,data=doencas_data)
        if doencas_serializer.is_valid():
            doencas_serializer.save()
            return JsonResponse("Editado com sucesso",safe=False)
        return JsonResponse("Falha ao editar", safe=False)
    elif request.method=='DELETE':
        doenca=Doencas.objects.get(id=pathId)
        doenca.delete()
        return JsonResponse("Deletado com sucesso",safe=False)

@csrf_exempt
def usuariosApi(request,email=0,pathId=0):
    if request.method=='GET':
        if email==0:
            usuarios = Usuarios.objects.all()
            usuarios_serializer=UsuariosSerializers(usuarios,many=True)
            return JsonResponse(usuarios_serializer.data,safe=False)
        else:
            usuario=Usuarios.objects.get(email=email)
            usuarios_serializer=UsuariosSerializers(usuario)
            return JsonResponse(usuarios_serializer.data,safe=False)
    elif request.method=='POST':
        usuarios_data=JSONParser().parse(request)
        usuarios_serializer=UsuariosSerializers(data=usuarios_data)
        if usuarios_serializer.is_valid():
            usuarios_serializer.save()
            return JsonResponse("Adicionado com sucesso",safe=False)
        return JsonResponse("Falha ao adicionar", safe=False)
    elif request.method=='PUT':
        usuarios_data=JSONParser().parse(request)
        usuario=Usuarios.objects.get(id=usuarios_data['id'])
        usuarios_serializer=UsuariosSerializers(usuario,data=usuarios_data)
        if usuarios_serializer.is_valid():
            usuarios_serializer.save()
            return JsonResponse("Editado com sucesso",safe=False)
        return JsonResponse("Falha ao editar", safe=False)
    elif request.method=='DELETE':
        usuario=Usuarios.objects.get(id=pathId)
        usuario.delete()
        return JsonResponse("Deletado com sucesso",safe=False)