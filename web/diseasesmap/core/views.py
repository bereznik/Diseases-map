from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest
import json, os

from types import SimpleNamespace
from django.contrib import messages
from server import views, serializers


def dashboard(request):
    return render(request, 'dashboard.html', {})


def about_restrict(request):
    return render(request, 'about_restrict.html', {})


def contact_restrict(request):
    return render(request, 'contact_restrict.html', {})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        myRequest = HttpRequest()
        myRequest.method = 'GET'

        try:
            jsonResponse = views.usuariosApi(myRequest, username)
            dictResponse = json.loads(
                jsonResponse.content, object_hook=lambda d: SimpleNamespace(**d))
            if password == dictResponse.senha:
                return index(request)
            else:
                messages.error(request, "Senha não encontrada")
                return render(request, 'login.html', {})
        except:
            messages.error(request, "Usuário não encontrado")

    return render(request, 'login.html', {})


def index(request):
    return render(request, 'index.html', {})


def notifications(request):
    return render(request, 'notifications.html', {})


def account(request):
    return render(request, 'account.html', {})


@csrf_exempt
def usertable(request):
    if request.method == 'POST':
        dictResponse = {
            "posto": request.POST['posto'],
            "nome": request.POST['nome'],
            "nomeguerra": request.POST['nomeguerra'],
            "email": request.POST['email'],
            "senha": request.POST['senha'],
            "om": request.POST['om'],
            "foto": "teste"
        }

        try:
            usuarios_serializer = serializers.UsuariosSerializers(
                data=json.dumps(dictResponse))
            print(json.dumps(dictResponse))
            if usuarios_serializer.is_valid():
                usuarios_serializer.save()
                messages.success("Usuário adicionado com sucesso")
            else:
                print("ERRO")
        except:
            messages.error(request, "Falha no cadastro de novo usuário")
    return render(request, 'user_table.html', {})


def diseases(request):
    if request.method == 'POST':
        dictResponse = {
            "nome": request.POST['nome'],
            "vacinadisp": request.POST['vacinadisp'],
            "descricao": request.POST['descricao'],
            "link": request.POST['link']
        }
        try:
            views.doencasApi(json.dumps(dictResponse))
            messages.success("Doença adicionada com sucesso")
        except:
            messages.error(request, "Falha no cadastro de nova doença")
    return render(request, 'diseases.html', {})

def populate(request):
    # usersFile = open(os.path.realpath(os.path.join(os.path.dirname(__file__), 'xslx', 'users.json')))
    # users = json.load(usersFile)
    # for user in users:
    #     print(user)
    #     usuarios_serializer=serializers.UsuariosSerializers(data=user)
    #     if usuarios_serializer.is_valid():
    #         usuarios_serializer.save()

    # localidadesFile = open(os.path.realpath(os.path.join(os.path.dirname(__file__), 'xslx', 'localidades.json')))
    # localidades = json.load(localidadesFile)
    # for localidade in localidades:
    #     print(localidade)
    #     localidades_serializer=serializers.LocalidadesSerializers(data=localidade)
    #     if localidades_serializer.is_valid():
    #         localidades_serializer.save()
    #     else:
    #         print("ERRO")
    #         return render(request, 'populate.html', {})
   
    # doencasFile = open(os.path.realpath(os.path.join(os.path.dirname(__file__), 'xslx', 'doencas.json')))
    # doencas = json.load(doencasFile)
    # for doenca in doencas:
    #     print(doenca)
    #     doencas_serializer=serializers.DoencasSerializers(data=doenca)
    #     if doencas_serializer.is_valid():
    #         doencas_serializer.save()
    #     else:
    #         print("ERRO")
    #         return render(request, 'populate.html', {})

    return render(request, 'populate.html', {})
