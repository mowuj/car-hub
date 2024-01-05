from django.shortcuts import render,redirect
from .models import Brand
from . forms import BrandForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

class AddBrandView(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'add_brand.html'
    success_url = reverse_lazy('add_brand')

    def form_valid(self, form):
        return super().form_valid(form)
