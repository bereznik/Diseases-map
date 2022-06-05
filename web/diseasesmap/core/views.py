from django.forms import formset_factory
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest
from itsdangerous import json
import pandas as pd
import mysql.connector as sql

from types import SimpleNamespace
from django.contrib import messages
from server import views

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
        jsonResponse = views.usuariosApi(myRequest,username)
        dictResponse = json.loads(jsonResponse.content, object_hook=lambda d: SimpleNamespace(**d))
        
        if password == dictResponse.senha:
            return index(request)
        else:
            messages.error(request,"Usuário e senha não encontrados")
            return render(request, 'login.html', {})
            
    return render(request, 'login.html', {})

def index(request):
    return render(request, 'index.html', {})

def notifications(request):
    db_connection = sql.connect(host='127.0.0.1', database='diseasesmapdb', user='diseasesmapadmin',
                                password='diseasesmap')
    dataframe = pd.read_sql('select l.cidade, d.nome, nt.casos from ' +
                            '(( server_notificacoestotal as nt join server_doencas as d ' +
                            'on (nt.iddoenca = d.id))' +
                            'join server_localidades as l on (l.id = nt.idmunicipio))', con=db_connection)
    notificacoes = dataframe.to_dict('records')
    context = {
        'notificacoes': notificacoes
    }
    return render(request, 'notifications.html', context)

def account(request):
    return render(request, 'account.html', {})

def usertable(request):
    myRequest = HttpRequest()
    myRequest.method = 'GET'
    jsonResponse = views.usuariosApi(myRequest)
    noDictResponseApi = json.loads(jsonResponse.content, object_hook=lambda d: SimpleNamespace(**d))
    dict = []
    for namespace in noDictResponseApi:
        dict.append(vars(namespace))
    context = {
        'users' : dict
    }
    return render(request, 'user_table.html', context)

def diseases(request):
    return render(request, 'diseases.html', {})