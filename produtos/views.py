from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def catalogo(request):
    return render(request, 'catalogo.html')