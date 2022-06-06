from django.forms import formset_factory
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest
from django.core.paginator import Paginator

from cmath import exp
from distutils.log import error
import json
import os
import pandas as pd
import mysql.connector as sql


from types import SimpleNamespace
from django.contrib import messages
from server import views, serializers
from server.models import Localidades, Notificacoes, Doencas, Usuarios

def authorization(request):
    try:
        myRequest = HttpRequest()
        myRequest.method = 'GET'
        username = request.COOKIES.get('user')
        jsonResponse = views.usuariosApi(myRequest, username)
        print(jsonResponse)
        dictResponse = json.loads(jsonResponse.content, object_hook=lambda d: SimpleNamespace(**d))
        return dictResponse
    except:
        print("aqui")
        return error


def logout(request):
    response = login(request)
    response.set_cookie("user","")
    return response



def dashboard(request):
    return render(request, 'dashboard.html', {})


def about_restrict(request):
    return render(request, 'about_restrict.html', {})


def contact_restrict(request):
    return render(request, 'contact_restrict.html', {})


def about(request):
    myUser = authorization(request)
    if myUser==error:
        return login(request)
    context = {
        'myUser': myUser
    }
    return render(request, 'about.html', context)

def contact(request):
    myUser = authorization(request)
    if myUser==error:
        return login(request)
    context = {
        'myUser': myUser
    }
    return render(request, 'contact.html', context)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        myRequest = HttpRequest()
        myRequest.method = 'GET'

        try:
            jsonResponse = views.usuariosApi(myRequest, username)
            dictResponse = json.loads(jsonResponse.content, object_hook=lambda d: SimpleNamespace(**d))
            if password == dictResponse.senha:
                response = index(request)
                response.set_cookie("user",username)
                return response
            else:
                messages.error(request, "Senha não encontrada")
                return render(request, 'login.html', {})
        except:
            messages.error(request, "Usuário não encontrado")

    return render(request, 'login.html', {})


def index(request):
    myUser = authorization(request)
    if myUser==error:
        return login(request)
    context = {
        'myUser': myUser
    }
    return render(request, 'index.html', context)


@csrf_exempt
def notifications(request):
    myUser = authorization(request)
    if myUser==error:
        return login(request)

    db_connection = sql.connect(host='127.0.0.1', database='diseasesmapdb', user='diseasesmapadmin',
                                password='diseasesmap')
    if request.method == 'POST':
        casos = request.POST['casos']
        nomedoenca_id = request.POST['nomedoenca_id']
        nomemunicipio = request.POST['nomemunicipio']
        nomeestado = request.POST['nomeestado']
        id = pd.read_sql('select id from diseasesmapdb.server_localidades'
                         + ' where nome = "' + nomemunicipio + '" and estado = "' + nomeestado + '"', con=db_connection)
        idmunicipio_id = id.to_dict('records')[0]

        dictResponse = {
            "idmunicipio": idmunicipio_id['id'],
            "nomedoenca": nomedoenca_id,
            "casos": casos
        }
        jsonContent = json.loads(json.dumps(dictResponse))

        try:
            notifications_serializer = serializers.NotificacoesSerializers(
                data=jsonContent)
            if notifications_serializer.is_valid():
                notifications_serializer.save()
                messages.success("Notificação adicionada com sucesso")
        except:
            messages.error(request, "Falha no cadastro de nova notificação")

    myRequest = HttpRequest()
    myRequest.method = 'GET'

    nome = 'select l.nome, nt.nomedoenca_id, nt.casos from diseasesmapdb.server_notificacoes as nt join diseasesmapdb.server_localidades as l on nt.idmunicipio_id = l.id'
    dataframe = pd.read_sql(nome, con=db_connection)
    notifications = dataframe.to_dict('records')

    paginator = Paginator(notifications, 100)
    page_number = request.GET.get('page')
    notifications = paginator.get_page(page_number)

    context = {
        'notifications': notifications,
        'myUser': myUser
    }

    return render(request, 'notifications.html', context)


def account(request):
    myUser = authorization(request)
    if myUser==error:
        return login(request)
    context = {
        'myUser': myUser
    }
    return render(request, 'account.html', context)

@csrf_exempt
def usertable(request, pathId=0):
    myUser = authorization(request)
    if myUser==error:
        return login(request)

    if request.method == 'POST':
        if pathId != 0:
            try:
                usuario = Usuarios.objects.get(id=pathId)
                usuario.delete()
                messages.success("Usuário removido com sucesso")
                usertable(HttpRequest())
            except:
                messages.error(request, "Falha na remocao de novo usuário")
                usertable(HttpRequest())
        else:
            dictResponse = {
                "posto": request.POST['posto'],
                "nome": request.POST['nome'],
                "nomeguerra": request.POST['nomeguerra'],
                "email": request.POST['email'],
                "senha": request.POST['senha'],
                "om": request.POST['om'],
                "foto": ""
            }
            jsonContent = json.loads(json.dumps(dictResponse))

            try:
                usuarios_serializer = serializers.UsuariosSerializers(
                    data=jsonContent)
                if usuarios_serializer.is_valid():
                    usuarios_serializer.save()
                    messages.success("Usuário adicionado com sucesso")
                    usertable(HttpRequest())
            except:
                messages.error(request, "Falha no cadastro de novo usuário")
                usertable(HttpRequest())

    myRequest = HttpRequest()
    myRequest.method = 'GET'
    jsonResponse = views.usuariosApi(myRequest)
    noDictResponseApi = json.loads(
        jsonResponse.content, object_hook=lambda d: SimpleNamespace(**d))
    dict = []
    for namespace in noDictResponseApi:
        dict.append(vars(namespace))
    paginator = Paginator(dict, 10)
    page_number = request.GET.get('page')
    users = paginator.get_page(page_number)

    context = {
        'users': users,
        'myUser': myUser
    }

    return render(request, 'user_table.html', context)


@csrf_exempt
def diseases(request):
    myUser = authorization(request)
    if myUser==error:
        return login(request)

    if request.method == 'POST':
        dictResponse = {
            "nome": request.POST['nome'],
            "vacinadisp": request.POST['vacinadisp'],
            "descricao": request.POST['descricao'],
            "link": request.POST['link']
        }
        jsonContent = json.loads(json.dumps(dictResponse))

        try:
            doencas_serializer = serializers.DoencasSerializers(
                data=jsonContent)
            if doencas_serializer.is_valid():
                doencas_serializer.save()
                messages.success("Doença adicionada com sucesso")
        except:
            messages.error(request, "Falha no cadastro de nova doença")
    myRequest = HttpRequest()
    myRequest.method = 'GET'
    jsonResponse = views.doencasApi(myRequest)
    noDictResponseApi = json.loads(
        jsonResponse.content, object_hook=lambda d: SimpleNamespace(**d))
    dict = []
    for namespace in noDictResponseApi:
        dict.append(vars(namespace))
    paginator = Paginator(dict, 10)
    page_number = request.GET.get('page')
    diseases = paginator.get_page(page_number)

    context = {
        'diseases': diseases,
        'myUser': myUser
    }

    return render(request, 'diseases.html', context)


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

    notificacoesFile = open(os.path.realpath(os.path.join(
        os.path.dirname(__file__), 'xslx', 'notificacoes.json')))
    notificacoes = json.load(notificacoesFile)
    for notificacao in notificacoes:
        print(notificacao)
        notificacoes_serializer = serializers.NotificacoesSerializers(
            data=notificacao)
        if notificacoes_serializer.is_valid():
            notificacoes_serializer.save()
        else:
            print("ERRO")
            return render(request, 'populate.html', {})

    return render(request, 'populate.html', {})
