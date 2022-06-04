from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest
import json

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


def usertable(request):
    return render(request, 'user_table.html', {})


def diseases(request):
    return render(request, 'diseases.html', {})
