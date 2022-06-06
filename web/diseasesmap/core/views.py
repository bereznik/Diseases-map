from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest
import json, os
import pandas as pd
from types import SimpleNamespace
from django.contrib import messages
from server import views, serializers


def dashboard(request):
    json = get_notifications()
    data = {"chave":json};
    return render(request, 'dashboard.html', data)


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
    json = get_notifications()
    data = {"chave":json};
    return render(request, 'index.html', data)


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
            "foto": ""
        }
        jsonContent = json.loads(json.dumps(dictResponse))
        print(jsonContent)

        try:
            usuarios_serializer = serializers.UsuariosSerializers(data=jsonContent)
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

def get_notifications():
    QUERY = ''' SELECT l.longitude AS long, l.latitude AS lat, l.nome as municipio, n.nomedoenca AS nomedoenca, n.casos AS casosTotais
                FROM Notificacoes n JOIN Localidades l ON n.idmunicipio = l.id '''

    df = pd.DataFrame(data ={'lat':[-22.9068,-22.9068,1,1],'long':[-43.1729,-43.1729,3,3],'municipio':['rio','rio','sp','sp'],
    'nome':['Dengue','Chicungunha','Dengue','COVID'],'casosTotais':[1,2,3,4]})

    cols = ['lat','long','municipio']
    json = df.groupby(cols).apply(lambda g: g.drop(cols, axis=1).to_dict('records')).reset_index().rename({0:'doencas'}, axis=1).to_dict('records')
    return json
    

