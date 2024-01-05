from django.shortcuts import render, redirect, get_object_or_404
from .models import Car
from .forms import CarForm
from customer.forms import CommentForm
from django.views.generic import CreateView,UpdateView,DetailView
from django.urls import reverse_lazy
from django.views import View

class AddCarView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'add_car.html'
    success_url = reverse_lazy('add_car')

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)


class CarDetailView(DetailView):
    model = Car
    pk_url_kwarg = 'id'
    template_name = 'car_detail.html'

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
            return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.get_object()
        comments = car.comments.all()
        comment_form = CommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

def buy_car(request,id):
    car = Car.objects.get(pk=id)
    if car.quantity > 0:
        car.quantity -= 1
        car.save()
    return redirect('car_detail', id=car.id)
