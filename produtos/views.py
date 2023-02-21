from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto, Categoria

# Create your views here.

def catalogo(request):
    if request.method == "GET":
        produtos = Produto.objects.all()
        categoria = Categoria.objects.all()
    return render(request, 'catalogo.html', {'produtos':produtos, 'categoria':categoria})