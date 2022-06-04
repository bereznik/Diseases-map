from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def dashboard(request):
    return render(request, 'dashboard.html', {})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        if username=='may@ime.br' and password=='123':
            return index(request)

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