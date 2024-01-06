from django.shortcuts import render,redirect
from .models import Brand
from . forms import BrandForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class AddBrandView(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'add_brand.html'
    success_url = reverse_lazy('add_brand')

    def form_valid(self, form):
        return super().form_valid(form)
