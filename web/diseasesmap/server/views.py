from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from server.models import Doencas
from server.serializers import DoencasSerializers

# Create your views here.

@csrf_exempt
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


