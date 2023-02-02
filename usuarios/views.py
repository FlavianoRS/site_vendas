from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirSenha = request.POST.get('confirSenha')
        
        return HttpResponse(f'Nome: {nome}\n Email:{email}\n Senha:{senha}')
    else:
        return render(request, 'login.html')