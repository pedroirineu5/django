from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarForm
from django.views import View
from django.views.generic import CreateView, ListView, DetailView


class ListCarsView(ListView):
    
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        
        if search:
            cars = cars.filter(model_icontains=search)
        
        return cars

class CreateNewCarView(CreateView):
    
    model = Car
    form_class = CarForm
    template_name = 'new_car.html'
    success_url = '/car_list/'


class CarDetailView(DetailView):

    model = Car
    template_name = 'car_detail.html'