from django.shortcuts import render
from cars.models import Car


def cars_view(request):
    cars = Car.objects.all()
    search = request.GET.get('search')
    
    if search:     
        # e uma queryset, nao apenas uma 
        cars = Car.objects.filter(model__contains = search)

    return render(
        request,
        'cars.html',
        {'cars': cars }
        )