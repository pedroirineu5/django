from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home/index.html')


def home2(request):
    return render(request, 'global/base.html')   