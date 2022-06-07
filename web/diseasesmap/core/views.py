from django.forms import formset_factory
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest
from django.core.paginator import Paginator
from rest_framework.parsers import JSONParser

from cmath import exp
from distutils.log import error
import json
import os
import pandas as pd
import mysql.connector as sql


from types import SimpleNamespace
from django.contrib import messages
from server import views, serializers
from server.models import Notificacoes, Doencas, Usuarios

def authorization(request):
    username = request.COOKIES.get('user')
    print(username)
    try:
        myRequest = HttpRequest()
        myRequest.method = 'GET'
        jsonResponse = views.usuariosApi(myRequest, username, 0)
        print(jsonResponse)
        dictResponse = json.loads(jsonResponse.content, object_hook=lambda d: SimpleNamespace(**d))
        return dictResponse
    except:
        return error


def logout(request):
    response = login(request)
    response.set_cookie("user","")
    return response

def dashboard(request):
    # myUser = authorization(request)
    # if myUser==error:
    #     return login(request)

    jsonNotifications = get_notifications()
    
    myRequest = HttpRequest()
    myRequest.method = 'GET'
    jsonResponse = views.doencasApi(myRequest)
    noDictResponseApi = json.loads(jsonResponse.content, object_hook=lambda d: SimpleNamespace(**d))
    dict_doencas = []
    for namespace in noDictResponseApi:
        dict_doencas.append(vars(namespace))

    count=0
    for disease in dict_doencas:
        disease["id"]=count
        disease["vacinadisp"]="false"
        count=count+1

    context = {
        'diseases': dict_doencas,
        #'myUser': myUser,
        'chave': jsonNotifications
    }
    return render(request, 'dashboard.html', context)


def about_restrict(request):
    return render(request, 'about_restrict.html', {})


def contact_restrict(request):
    return render(request, 'contact_restrict.html', {})


def about(request):
    # myUser = authorization(request)
    # if myUser!=error:
    #     context = {
    #         'myUser': myUser
    #     }
    #     return render(request, 'about.html', context)
    return render(request, 'about.html')

def contact(request):
    # myUser = authorization(request)
    # if myUser==error:
    #     return login(request)
    context = {
        #'myUser': myUser
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
    # myUser = authorization(request)
    # if myUser==error:
    #     return login(request)

    jsonNotifications = get_notifications()
    
    myRequest = HttpRequest()
    myRequest.method = 'GET'
    jsonResponse = views.doencasApi(myRequest)
    noDictResponseApi = json.loads(jsonResponse.content, object_hook=lambda d: SimpleNamespace(**d))
    dict_doencas = []
    for namespace in noDictResponseApi:
        dict_doencas.append(vars(namespace))

    count=0
    for disease in dict_doencas:
        disease["id"]=count
        disease["vacinadisp"]="false"
        count=count+1

    context = {
        'diseases': dict_doencas,
        #'myUser': myUser,
        'chave': jsonNotifications
    }
    return render(request, 'index.html', context)



@csrf_exempt
def notifications(request,pathId=0):
    # myUser = authorization(request)
    # if myUser==error:
    #     return login(request)

    db_connection = sql.connect(host='127.0.0.1', database='diseasesmapdb', user='diseasesmapadmin',
                                password='diseasesmap')
    if request.method == 'POST':
        if pathId!=0:
            try:
                notificacao = Notificacoes.objects.get(id=pathId)
                notificacao.delete()
            except:
                error
        else:
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
            except:
                error

    myRequest = HttpRequest()
    myRequest.method = 'GET'

    nome = 'select l.nome, nt.nomedoenca_id, nt.casos, nt.id from diseasesmapdb.server_notificacoes as nt join diseasesmapdb.server_localidades as l on nt.idmunicipio_id = l.id'
    dataframe = pd.read_sql(nome, con=db_connection)
    notifications = dataframe.to_dict('records')

    paginator = Paginator(notifications, 100)
    page_number = request.GET.get('page')
    notifications = paginator.get_page(page_number)

    context = {
        'notifications': notifications,
        ##'myUser': myUser
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
def user_edit(request,pathId=0):
    if request.method == 'POST':
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
        usuarios=Usuarios.objects.get(id=pathId)
        usuarios_serializer=serializers.UsuariosSerializers(usuarios,data=jsonContent)
        if usuarios_serializer.is_valid():
            usuarios_serializer.save()
        else:
            print("erroaqui")
        return usertable(HttpRequest())

    if pathId!=0:
        myRequest = HttpRequest()
        myRequest.method = 'GET'

        try:
            jsonResponse = views.usuariosApi(myRequest, 0, pathId)
            dictResponse = json.loads(jsonResponse.content, object_hook=lambda d: SimpleNamespace(**d))
        except:
            error

        context = {
            'user': dictResponse
        }
        return render(request, 'user_edit.html',context)

    return render(request, 'user_edit.html')


@csrf_exempt
def usertable(request, pathId=0):
    # myUser = authorization(request)
    # if myUser==error:
    #     return login(request)

    if request.method == 'POST':
        if pathId != 0:
            try:
                usuario = Usuarios.objects.get(id=pathId)
                usuario.delete()
                error
                usertable(HttpRequest())
            except:
                error
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
                    usertable(HttpRequest())
            except:
                error
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
        #'myUser': myUser
    }

    return render(request, 'user_table.html', context)

@csrf_exempt
def disease_edit(request,pathId=0):
    if request.method == 'POST':
        print("resposta vacina disp:::",request.POST['vacinadisp'])
        dictResponse = {
            "nome": request.POST['nome'],
            "vacinadisp": (request.POST['vacinadisp']=="on"),
            "descricao": request.POST['descricao'],
            "link": request.POST['link']
        }
        jsonContent = json.loads(json.dumps(dictResponse))
        doenca=Doencas.objects.get(nome=pathId)
        doencas_serializer=serializers.DoencasSerializers(doenca,data=jsonContent)
        if doencas_serializer.is_valid():
            doencas_serializer.save()
        else:
            print("erroaqui")
        return diseases(HttpRequest())

    if pathId!=0:
        myRequest = HttpRequest()
        myRequest.method = 'GET'

        try:
            jsonResponse = views.doencasApi(myRequest, pathId)
            dictResponse = json.loads(jsonResponse.content, object_hook=lambda d: SimpleNamespace(**d))
        except:
            error

        context = {
            'disease': dictResponse
        }
        return render(request, 'disease_edit.html',context)

    return render(request, 'disease_edit.html')

@csrf_exempt
def diseases(request,pathId=0):
    # myUser = authorization(request)
    # if myUser==error:
    #     return login(request)

    if request.method == 'POST':
        if pathId != 0:
            try:
                doenca = Doencas.objects.get(nome=pathId)
                doenca.delete()
            except:
                error
        else:
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
            except:
                error
        
    myRequest = HttpRequest()
    myRequest.method = 'GET'
    jsonResponse = views.doencasApi(myRequest)
    noDictResponseApi = json.loads(
        jsonResponse.content, object_hook=lambda d: SimpleNamespace(**d))
    dict = []
    for namespace in noDictResponseApi:
        dict.append(vars(namespace))
    paginator = Paginator(dict, 6)
    page_number = request.GET.get('page')
    diseases = paginator.get_page(page_number)

    context = {
        'diseases': diseases,
        #'myUser': myUser
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

    localidadesFile = open(os.path.realpath(os.path.join(os.path.dirname(__file__), 'xslx', 'localidades.json')))
    localidades = json.load(localidadesFile)
    for localidade in localidades:
        print(localidade)
        localidades_serializer=serializers.LocalidadesSerializers(data=localidade)
        if localidades_serializer.is_valid():
            localidades_serializer.save()
        else:
            print("ERRO")
            return render(request, 'populate.html', {})

    doencasFile = open(os.path.realpath(os.path.join(os.path.dirname(__file__), 'xslx', 'doencas.json')))
    doencas = json.load(doencasFile)
    for doenca in doencas:
        print(doenca)
        doencas_serializer=serializers.DoencasSerializers(data=doenca)
        if doencas_serializer.is_valid():
            doencas_serializer.save()
        else:
            print("ERRO")
            return render(request, 'populate.html', {})

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

def get_notifications():
    
    db_connection = sql.connect(host='127.0.0.1', database='diseasesmapdb', user='diseasesmapadmin',
                                password='diseasesmap')
    
    QUERY = ''' SELECT l.longitude AS lon, l.latitude AS lat, l.nome as municipio, n.nomedoenca_id AS nomedoenca, n.casos AS casosTotais
                FROM server_notificacoes n JOIN server_localidades l ON n.idmunicipio_id = l.id WHERE n.casos!=0'''

    df = pd.read_sql(QUERY,db_connection)
    
    # df = pd.DataFrame(data ={'lat':[-22.9068,-22.9068,1,1],'lon':[-43.1729,-43.1729,3,3],'municipio':['rio','rio','sp','sp'],
    # 'nome':['Dengue','Chicungunha','Dengue','COVID'],'casosTotais':[1,2,3,4]})

    cols = ['lat','lon','municipio']
    json = df.groupby(cols).apply(lambda g: g.drop(cols, axis=1).to_dict('records')).reset_index().rename({0:'doencas'}, axis=1).to_dict('records')
    return json
    

