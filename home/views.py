from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.

def home(request):

    context = {
        'text' : 'Pagina Inicial'
    }

    return render(request,'home/index.html', context)


def home2(request):

    context = {
        'text' : 'Pagina de Exemplo 1',
        'title' : 'Agora estou foda'
    }

    return render(request, 'home/exemplo1.html', context)