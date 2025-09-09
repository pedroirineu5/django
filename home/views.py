from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("UMA MENSAGEM PARA ALGUÉM MUITO FODA, DIRETAMENTO DO VIEWS DO APP HOME!")