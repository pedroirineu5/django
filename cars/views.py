from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarForm
from django.views import View
from django.views.generic import ListView

class CarsView(View):

    def get(self, request):
        
        cars = Car.objects.all().order_by('model')
        # essa busca que acontece em uma URL usando 
        # http://localhost:8000/cars/?search=Teste
        search = request.GET.get('search')
    
        if search:     
         # e uma queryset, nao apenas uma lista comum
             cars = Car.objects.filter(model__icontains = search).order_by('model')

        return render(
            request,
            'cars.html',
            {'cars': cars }
            )

class ListCarsView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

class NewCarView(View):

    def get(self, request):
        new_car_form = CarForm()
        return render(request, 'new_car.html', {'new_car_form' : new_car_form})
    
    def post(self, request):   
        new_car_form = CarForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        return render(request, 'new_car.html', {'new_car_form' : new_car_form})