from django.http import HttpResponse

def cars_view(request):
    return HttpResponse('Respondendo do outro mundo')
