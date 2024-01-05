from django.shortcuts import render
from .models import Car
from .forms import CarForm
from django.views.generic import CreateView,UpdateView,DetailView
from django.urls import reverse_lazy

class AddCarView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'add_car.html'
    success_url = reverse_lazy('add_car')

class CarDetailView(DetailView):
    model=Car
    pk_url_kwarg='id'
    template_name='car_detail.html'
